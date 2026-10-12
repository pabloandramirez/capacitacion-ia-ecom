from django.db import models
from django.utils import timezone


class Plomero(models.Model):
    sucursal = models.PositiveSmallIntegerField(verbose_name="Sucursal")
    cuil = models.BigIntegerField(verbose_name="CUIL")
    nombre = models.CharField(max_length=20, verbose_name="Apellido y nombre")
    desde = models.DateField(null=True, blank=True, verbose_name="Vigencia desde")
    hasta = models.DateField(null=True, blank=True, verbose_name="Vigencia hasta")

    class Meta:
        db_table = "plomer"
        verbose_name = "Plomero"
        verbose_name_plural = "Plomeros"
        ordering = ["sucursal", "cuil"]
        constraints = [
            models.UniqueConstraint(
                fields=["sucursal", "cuil"], name="iplomer"
            )
        ]

    def __str__(self):
        return f"{self.sucursal}-{self.cuil} {self.nombre}".strip()

    @property
    def cuil_formateado(self):
        s = str(self.cuil).zfill(11)
        return f"{s[:2]}-{s[2:10]}-{s[10]}"

    @property
    def estado_vigencia(self):
        if self.hasta is None:
            return "abierta"
        hoy = timezone.localdate()
        if self.hasta < hoy:
            return "vencido"
        if (self.hasta - hoy).days <= 90:
            return "por-vencer"
        return "vigente"

    @property
    def estado_label(self):
        return {
            "vigente": "Vigente",
            "por-vencer": "Por vencer",
            "vencido": "Vencido",
            "abierta": "Sin vencimiento",
        }[self.estado_vigencia]

    @property
    def vigencia_pct(self):
        if self.desde is None:
            return 0
        if self.hasta is None or self.hasta <= self.desde:
            return 100
        hoy = timezone.localdate()
        total = (self.hasta - self.desde).days
        elapsed = (hoy - self.desde).days
        return max(0, min(100, int(elapsed * 100 / total)))


class Documento(models.Model):
    codigo = models.PositiveSmallIntegerField(verbose_name="Código")
    nombre = models.CharField(max_length=30, verbose_name="Descripción")

    class Meta:
        db_table = "documento"
        verbose_name = "Tipo de documento"
        verbose_name_plural = "Tipos de documento"
        ordering = ["codigo"]

    def __str__(self):
        return f"{self.codigo} {self.nombre}".strip()
