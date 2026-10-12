# 05 - Plan de migración paso a paso

Cada fase produce un resultado verificable. No avanzar a la siguiente sin cumplir la verificación.

## Fase 0 — Preparación

1. Confirmar entorno: Python y Django instalados; proyecto en la raíz del repo.
2. Verificar que `db.sqlite3` y `manage.py` existen (ya presentes).
3. Crear/activar el entorno virtual (si no existe).
4. Instalar dependencias y registrar versiones.

**Verificación:** `python manage.py check` sin errores.

## Fase 1 — Creación de la app `plomeros`

1. `python manage.py startapp plomeros`
2. Agregar `'plomeros'` a `INSTALLED_APPS` en `abm_plomero/settings.py`.
3. Ajustar `settings.py`:
   - `LANGUAGE_CODE = 'es-ar'`
   - `TIME_ZONE = 'America/Argentina/Buenos_Aires'`
   - `USE_TZ = True`

**Verificación:** `python manage.py check` sin errores.

## Fase 2 — Modelo de datos

1. Implementar `Plomero` en `plomeros/models.py` (ver [02-modelo-de-datos.md](02-modelo-de-datos.md)).
2. (Opcional) implementar `Documento` como entidad de solo lectura.
3. Crear migración: `python manage.py makemigrations plomeros`.
4. Aplicar: `python manage.py migrate`.
5. Registrar el modelo en `plomeros/admin.py`.

**Verificación:**
- `python manage.py showmigrations plomeros` muestra la migración aplicada.
- La tabla `plomer` existe en `db.sqlite3` con PK `(sucursal, cuil)`.

## Fase 3 — Carga de datos

1. Implementar `plomeros/management/commands/cargar_plomeros.py`.
2. Ejecutar `python manage.py cargar_plomeros --path PLOMER_202609291133.csv`.
3. Validar conteos según [04-carga-datos-iniciales.md](04-carga-datos-iniciales.md) §7.

**Verificación:**
- 64 registros cargados.
- 3 registros con `hasta IS NULL`.
- Sin duplicados `(sucursal, cuil)`.
- Re-ejecutar el comando **no** duplica registros.

## Fase 4 — Home / listado de Plomeros (equivalente a `PloBus2`)

1. Crear `plomeros/urls.py` y enlazarlo desde `abm_plomero/urls.py`.
2. Implementar vista de listado (ListView) con orden `(sucursal, cuil)`.
3. Crear template de listado con columnas: `Op`, CUIL, Nombre, Desde, Hasta.
4. Incluir barra de acciones (Alta) y por fila (Modificar / Baja).

**Verificación:** la lista muestra los 64 registros ordenados.

## Fase 5 — Alta / Modificación / Baja (transacción `PLOMER`)

1. Formulario (`ModelForm`) de alta/edición con los 5 campos.
2. Reglas:
   - `sucursal` no editable en edición.
   - `cuil` editable solo en alta.
   - `desde` precargado con la fecha de hoy en alta.
3. Vista de alta (`INS`), edición (`UPD`) y eliminación (`DLT`) con confirmación.
4. Mensajes de éxito/error.

**Verificación:** crear, modificar y eliminar funcionan y refrescan la lista.

## Fase 6 — Búsqueda / Prompt (`Gx0GW0`)

1. Formulario de filtros: sucursal (`>=`), código (`>=`), nombre (`LIKE`), desde (`>=`), hasta (`>=`).
2. Grilla de resultados ordenada por `(sucursal, cuil)`.
3. Acción de selección que devuelve `(sucursal, cuil)`.
4. Implementar como vista/modal popup.

**Verificación:** los filtros devuelven subconjuntos correctos; la selección retorna el par clave.

## Fase 7 — Pruebas

1. Tests de modelo: unicidad `(sucursal, cuil)`, nulos en fechas.
2. Test del comando de carga: conteo 64, idempotencia.
3. Tests de vistas: listado, alta, edición, baja, búsqueda.

**Verificación:** `python manage.py test` en verde.

## Fase 8 — Cierre

1. Revisar estilo/convenciones ([06-convenciones.md](06-convenciones.md)).
2. Documentar comandos en `README` o `AGENTS.md`.
3. Demo final sobre datos de ejemplo.

## Trazabilidad GX → Django

| Genexus | Django |
|---------|--------|
| Transacción `PLOMER` | Modelo `Plomero` + vistas CRUD |
| `PSucu` | Servicio/util para datos de sucursal |
| `TPLOMER` (INS/UPD/DLT) | Vistas de alta/edición/baja |
| WorkPanel `PloBus2` | Vista de listado + acciones |
| Prompt `Gx0GW0` | Vista de búsqueda/selección |
| Tabla `PLOMER` (608) | Tabla `plomer` (SQLite) |
| `Docu_*` | Modelo `Documento` (opcional, sin datos) |
