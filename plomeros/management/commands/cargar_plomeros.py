import csv
from datetime import date
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from plomeros.models import Plomero


def parse_date(raw):
    raw = (raw or "").strip()
    if not raw or raw == "00000000":
        return None
    return date(int(raw[0:4]), int(raw[4:6]), int(raw[6:8]))


class Command(BaseCommand):
    help = "Carga los plomeros desde el CSV de ejemplo (PLOMER_*.csv)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            type=str,
            default=None,
            help="Ruta del CSV. Por defecto: PLOMER_202609291133.csv en la raíz.",
        )
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Vacía la tabla plomer antes de cargar.",
        )

    def handle(self, *args, **options):
        if options["path"]:
            path = Path(options["path"])
        else:
            path = Path(settings.BASE_DIR) / "PLOMER_202609291133.csv"

        if not path.exists():
            raise CommandError(f"No se encontró el archivo: {path}")

        if options["flush"]:
            deleted, _ = Plomero.objects.all().delete()
            self.stdout.write(self.style.WARNING(f"Tabla vaciada: {deleted} registros eliminados."))

        created = updated = 0
        with path.open(encoding="utf-8", newline="") as fh, transaction.atomic():
            for row in csv.DictReader(fh):
                _, was_created = Plomero.objects.update_or_create(
                    sucursal=int(row["PLOSUCU"].strip()),
                    cuil=int(row["PLOCOD"].strip()),
                    defaults={
                        "nombre": row["PLONOM"].strip(),
                        "desde": parse_date(row["PLODES"]),
                        "hasta": parse_date(row["PLOHAS"]),
                    },
                )
                if was_created:
                    created += 1
                else:
                    updated += 1

        total = Plomero.objects.count()
        self.stdout.write(
            self.style.SUCCESS(
                f"Carga finalizada desde {path.name}: "
                f"{created} creados, {updated} actualizados, {total} en total."
            )
        )
