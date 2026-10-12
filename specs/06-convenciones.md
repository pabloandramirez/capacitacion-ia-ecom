# 06 - Convenciones y criterios de aceptación

## 1. Estructura del proyecto

```
abm_plomero/                  # configuración del proyecto (settings, urls, wsgi)
plomeros/                     # app de la migración
  migrations/
  templates/plomeros/         # templates de la app
  management/commands/        # cargar_plomeros.py
  models.py
  forms.py
  views.py
  urls.py
  admin.py
  tests.py
specs/                        # estos documentos
db.sqlite3
manage.py
PLOMER_202609291133.csv
duart20260929.xpw
```

## 2. Convenciones de código

- **Python/Django**: seguir PEP 8; nombres en inglés para código y español solo en textos visibles/etiquetas.
- **Modelos**: singular (`Plomero`); `db_table` en minúscula (`plomer`).
- **Campos**: nombres en español alineados al dominio (`sucursal`, `cuil`, `nombre`, `desde`, `hasta`).
- **Vistas**: preferir Class-Based Views (`ListView`, `CreateView`, `UpdateView`, `DeleteView`) salvo necesidad.
- **Templates**: `{% block %}` reutilizable con un `base.html`.
- **Idioma de UI**: español (`LANGUAGE_CODE = 'es-ar'`).
- **Sin comentarios** innecesarios en el código salvo lógica de negocio compleja.

## 3. Alineación con Genexus (reglas no negociables)

- Orden de la grilla: `PloSucu, PloCod, PloNom, PloDes, PloHas`.
- Orden de ordenamiento: `(sucursal, cuil)`.
- PK compuesta `(sucursal, cuil)`.
- `desde` = hoy por defecto en alta.
- `sucursal` no editable en transacción; `cuil` no editable en modificación/baja.
- Filtros de búsqueda: `>=` para sucursal/código/fechas y `LIKE` para nombre.

## 4. Comandos de desarrollo

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py cargar_plomeros --path PLOMER_202609291133.csv
python manage.py runserver
python manage.py test
python manage.py check
```

## 5. Criterios de aceptación

1. **Datos**: 64 plomeros en SQLite; 3 con `hasta` nulo; sin duplicados.
2. **Listado**: muestra todos los registros ordenados por `(sucursal, cuil)`.
3. **Alta**: crea un plomero con `desde` precargado en la fecha actual y `sucursal` fija.
4. **Modificación**: permite editar nombre/fechas; `cuil` y `sucursal` bloqueados.
5. **Baja**: elimina con confirmación previa.
6. **Búsqueda**: filtra por los 5 criterios con la semántica de las condiciones GX.
7. **Idempotencia de carga**: re-ejecutar `cargar_plomeros` no genera duplicados.
8. **Tests**: `python manage.py test` en verde.
9. **check**: `python manage.py check` sin advertencias.

## 6. Preguntas abiertas (a confirmar con el negocio)

1. ¿Se migra la entidad *Tipos de Documentos* (`Docu_*`) o se descarta?
2. ¿Debe validarse `hasta >= desde`? (no está en las reglas GX)
3. ¿Se requiere autenticación/permisos de usuario (operador)?
4. ¿Se desea replicar el look "terminal" o un diseño web estándar?
5. ¿Hay más sucursales además de la 1?
