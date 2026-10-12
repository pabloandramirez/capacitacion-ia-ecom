# 04 - Carga de datos iniciales (`PLOMER_202609291133.csv`)

## 1. Descripción del archivo

- Nombre: `PLOMER_202609291133.csv` (raíz del proyecto).
- 65 líneas: 1 encabezado + **64 registros**.
- Codificación: **UTF-8** (contiene `Ñ` en `QUIÑONES`, `VAÑEK`).
- Separador: coma. Todos los campos entre comillas dobles.

## 2. Encabezado y orden de columnas

```
"PLOCOD","PLODES","PLOHAS","PLONOM","PLOSUCU"
```

> **Importante:** el orden de columnas del CSV **NO** coincide con el orden de los atributos en la
> transacción. Se debe mapear **por nombre de encabezado**, no por posición.

## 3. Mapeo CSV → modelo `Plomero`

| Columna CSV | Campo Django | Tipo destino | Transformación |
|-------------|--------------|--------------|----------------|
| `PLOCOD` | `cuil` | BigInteger | `int(valor)` |
| `PLODES` | `desde` | Date / null | `YYYYMMDD` → `date`; `00000000` → `None` |
| `PLOHAS` | `hasta` | Date / null | `YYYYMMDD` → `date`; `00000000` → `None` |
| `PLONOM` | `nombre` | Char(20) | `valor.strip()` (quitar relleno de espacios) |
| `PLOSUCU` | `sucursal` | SmallInt | `int(valor)` |

## 4. Características verificadas de los datos

- Total: **64** registros.
- `PLOCOD`: sin duplicados; longitud máxima **11** dígitos.
  - Casos especiales con menos dígitos: `2` (SAMEEP / RELEV.) y `9999999999` (CONEXIONES VIEJA).
- `PLOSUCU`: único valor = **1** (sucursal 1).
- `PLONOM`: longitud máxima **20** (coincide con CharField(20)); vienen con relleno de espacios a la derecha.
  - Un valor contiene un sufijo tras espacios: `ROMERO RICARDO   -IV` (preservar tras `strip`).
- `PLODES`: ninguna fecha `00000000`; todas válidas.
- `PLOHAS`: **3** registros con `00000000` → se cargan como `NULL`:
  - `PLOCOD=2` (SAMEEP / RELEV.)
  - `DURE WALTER DANIEL`
  - `DOMINGUEZ NESTOR`

## 5. Reglas de parseo (pseudocódigo)

```python
def parse_date(raw: str):
    raw = raw.strip()
    if not raw or raw == "00000000":
        return None
    return date(int(raw[0:4]), int(raw[4:6]), int(raw[6:8]))

# lectura
with open(csv_path, encoding="utf-8", newline="") as fh:
    for row in csv.DictReader(fh):
        Plomero.objects.update_or_create(
            sucursal=int(row["PLOSUCU"]),
            cuil=int(row["PLOCOD"]),
            defaults={
                "nombre": row["PLONOM"].strip(),
                "desde": parse_date(row["PLODES"]),
                "hasta": parse_date(row["PLOHAS"]),
            },
        )
```

## 6. Estrategia de carga (a implementar en la fase de migración)

Opción recomendada: **management command** idempotente.

- Ubicación: `plomeros/management/commands/cargar_plomeros.py`
- Comportamiento:
  - Lee `PLOMER_202609291133.csv` (ruta configurable por argumento `--path`).
  - Usa `update_or_create` por `(sucursal, cuil)` → se puede re-ejecutar sin duplicar.
  - Reporta: insertados, actualizados, errores.
  - `--flush` opcional para vaciar la tabla antes de cargar.
- Ejecución:
  ```
  python manage.py cargar_plomeros --path PLOMER_202609291133.csv
  ```

Alternativa: fixtures JSON generadas a partir del CSV (menos flexible para `00000000`).

## 7. Validaciones posteriores a la carga

- `SELECT COUNT(*) FROM plomer` → **64**.
- `SELECT COUNT(*) FROM plomer WHERE hasta IS NULL` → **3**.
- `SELECT COUNT(DISTINCT sucursal)` → **1**.
- No debe existir más de un registro con el mismo `(sucursal, cuil)`.
- Verificar integridad de codificación (Ñ correcta en `QUIÑONES`, `VAÑEK`).

## 8. SQL de carga directa (referencia)

```sql
-- Ejemplo de filas (para verificación)
INSERT INTO plomer (sucursal, cuil, nombre, desde, hasta) VALUES
  (1, 20079166716, 'MARTINEZ PLACIDO A.', '2006-03-03', '2007-03-03'),
  (1, 2,           'SAMEEP / RELEV.',    '2016-09-01', NULL),
  (1, 27404487472, 'ROLON BRENDA LEONOR','2022-03-04', '2022-12-31');
```
