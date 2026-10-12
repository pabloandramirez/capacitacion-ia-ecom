# 02 - Modelo de datos y mapeo a Django

## 1. Entidad principal: PLOMER

Tabla física origen: `PLOMER` (Id 608). Clave primaria compuesta `(PloSucu, PloCod)`.

| Atributo GX | Columna | Tipo GX | Long. | Nullable | Descripción |
|-------------|---------|---------|-------|----------|-------------|
| `PloSucu` | `sucursal` | Numeric (Z9) | 2 | No | Sucursal |
| `PloCod` | `cuil` | Numeric (Z…9) | 11 | No | CUIL del plomero |
| `PloNom` | `nombre` | Character | 20 | Sí | Apellido y nombre |
| `PloDes` | `desde` | Date | 8 | Sí | Vigencia desde |
| `PloHas` | `hasta` | Date | 8 | Sí | Vigencia hasta |

## 2. Reglas de mapeo de tipos

| Genexus | Django / SQLite | Notas |
|---------|-----------------|-------|
| Numeric longitud 2 `Z9` | `PositiveSmallIntegerField` | Rango 0–99 |
| Numeric longitud 11 `ZZZZZZZZZZ9` | `BigIntegerField` | Rango 0–99999999999; entran valores de 2 y 10 dígitos del CSV |
| Character 20 | `CharField(max_length=20)` | Se normalizan espacios sobrantes |
| Date 8 (`YYYYMMDD`) | `DateField` | `00000000` → `NULL` |
| Claves dobles | `id` + `UniqueConstraint` | Django 5.2 no permite `CompositePrimaryKey` en el admin |

## 3. Entidad secundaria: Tipos de Documentos (`Docu`)

Referenciada por la UI del WorkPanel. **No hay transacción/tabla definida en el `.xpw`**, por lo que se modela como entidad externa opcional.

| Atributo GX | Columna | Tipo GX | Long. | Descripción |
|-------------|---------|---------|-------|-------------|
| `Docu_codigo` | `codigo` | Numeric (Z9) | 2 | Código de tipo de documento |
| `Docu_nombre` | `nombre` | Character | — | Descripción |

> Decisión de esta etapa: modelar `Documento` como entidad de solo lectura y **no** poblarla (no hay datos en el CSV). Se puede dejar para una etapa posterior.

## 4. Modelo Django propuesto

> **Decisión implementada (Fase 1-2):** se usa clave sustituta `id` + `UniqueConstraint (sucursal, cuil)`
> en lugar de `CompositePrimaryKey`, porque Django 5.2 **no permite registrar en el admin** modelos con
> clave primaria compuesta (`ImproperlyConfigured`). La unicidad de negocio `(sucursal, cuil)` se preserva
> con la restricción `iplomer`, heredada del índice GX.

Archivo: `plomeros/models.py`

```python
from django.db import models


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
```

Alternativa (descartada por incompatibilidad con el admin): `pk = models.CompositePrimaryKey("sucursal", "cuil")`.

## 5. DDL equivalente (SQL)

```sql
CREATE TABLE plomer (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    sucursal  SMALLINT      NOT NULL,
    cuil      BIGINT        NOT NULL,
    nombre    VARCHAR(20),
    desde     DATE,
    hasta     DATE,
    CONSTRAINT iplomer UNIQUE (sucursal, cuil)
);
```

Restricción única heredada de `IPLOMER (PloSucu, PloCod)`: `UNIQUE (sucursal, cuil)`.

## 6. Diccionario de datos / etiquetas de UI

| Campo | Etiqueta UI (origen) | Etiqueta web propuesta |
|-------|----------------------|------------------------|
| `sucursal` | `PloSucu` / `Sucursal` | Sucursal |
| `cuil` | `PloCod` / `CUIL` | CUIL |
| `nombre` | `PloNom` / `Apellido y Nombre` | Apellido y nombre |
| `desde` | `PloDes` / `Desde` | Vigencia desde |
| `hasta` | `PloHas` / `Hasta` | Vigencia hasta |

## 7. Validaciones de negocio a implementar

- `sucursal` obligatoria; `cuil` obligatorio.
- Unicidad de `(sucursal, cuil)`.
- `desde`/`hasta` pueden ser nulos (`00000000` en origen).
- En **alta**, `desde` se precarga con la fecha del día (regla `PloDes = &Today IF &Mode = 'INS'`).
- `cuil` no editable en modos modificación/baja.
- `sucursal` no editable en la transacción (se toma del contexto/parámetro).
- Opcional: `hasta` ≥ `desde` (a confirmar con el negocio; no está en las reglas GX).
