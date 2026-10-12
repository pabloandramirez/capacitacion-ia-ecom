# EVIDENCIA

## Integrantes del grupo

- Edgardo Duarte
- Miguel Maurich
- Pablo Ramirez

## Fecha y hora actual del sistema

Comando (Windows / PowerShell): `Get-Date`

Salida pegada tal cual:

```
lunes, 12 de octubre de 2026 10:56:23
```

## Versión de Opencode

Comando: `opencode --version`

Salida pegada tal cual:

```
1.18.35
```

## Listado de todos los archivos del proyecto

Comando (Windows / PowerShell):

```
Get-ChildItem -Recurse -File -Force | Where-Object { $_.FullName -notmatch '\\(node_modules|\.git|venv|\.venv|__pycache__|\.idea|\.mypy_cache|\.pytest_cache|dist|build)\\' } | Select-Object Length, LastWriteTime, FullName | Format-Table -AutoSize | Out-String -Width 400
```

Salida cruda y completa pegada tal cual:

```
Length LastWriteTime       FullName                                                                                                                                                                         
------ -------------       --------                                                                                                                                                                         
143360 12/10/2026 10:49:39 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\db.sqlite3                                             
 41567 02/10/2026 8:20:05  C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\duart20260929.xpw                                     
   689 12/10/2026 10:00:11 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\manage.py                                               
  3750 02/10/2026 8:24:33  C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\PLOMER_202609291133.csv                                 
   415 12/10/2026 10:00:11 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\abm_plomero\asgi.py                                     
  3384 12/10/2026 10:16:11 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\abm_plomero\settings.py                                 
   839 12/10/2026 10:34:24 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\abm_plomero\urls.py                                     
   415 12/10/2026 10:00:11 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\abm_plomero\wsgi.py                                     
     0 12/10/2026 10:00:11 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\abm_plomero\__init__.py                                 
   454 12/10/2026 10:16:19 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\plomeros\admin.py                                       
   154 12/10/2026 10:16:03 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\plomeros\apps.py                                       
  2821 12/10/2026 10:46:55 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\plomeros\forms.py                                      
  2318 12/10/2026 10:34:16 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\plomeros\models.py                                     
    63 12/10/2026 10:16:03 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\plomeros\tests.py                                      
   491 12/10/2026 10:46:59 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\plomeros\urls.py                                       
  3339 12/10/2026 10:46:58 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\plomeros\views.py                                      
     0 12/10/2026 10:16:03 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\plomeros\__init__.py                                    
     0 12/10/2026 10:26:35 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\plomeros\management\__init__.py                         
  2338 12/10/2026 10:26:39 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\plomeros\management\commands\cargar_plomeros.py         
     0 12/10/2026 10:26:36 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\plomeros\management\commands\__init__.py                
  1886 12/10/2026 10:16:41 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\plomeros\migrations\0001_initial.py                     
     0 12/10/2026 10:16:03 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\plomeros\migrations\__init__.py                         
  7956 12/10/2026 10:47:10 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\plomeros\static\plomeros\css\app.css                    
  1357 12/10/2026 10:40:48 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\plomeros\templates\plomeros\base.html                   
  1236 12/10/2026 10:41:01 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\plomeros\templates\plomeros\plomero_confirm_delete.html
  2289 12/10/2026 10:40:59 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\plomeros\templates\plomeros\plomero_form.html           
  2074 12/10/2026 10:47:09 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\plomeros\templates\plomeros\plomero_list.html           
  2629 12/10/2026 10:47:08 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\plomeros\templates\plomeros\plomero_search.html         
  7174 12/10/2026 10:11:15 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\specs\01-analisis-genexus.md                            
  4503 12/10/2026 10:17:06 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\specs\02-modelo-de-datos.md                             
  5204 12/10/2026 10:11:39 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\specs\03-estructura-visual-ui.md                        
  3837 12/10/2026 10:11:57 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\specs\04-carga-datos-iniciales.md                       
  3973 12/10/2026 10:12:06 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\specs\05-plan-migracion-paso-a-paso.md                  
  2848 12/10/2026 10:12:13 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\specs\06-convenciones.md                               
  9736 12/10/2026 10:26:35 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\specs\frontend-design-skill.md                          
  2243 12/10/2026 10:10:56 C:\Users\BANGHO\Desktop\Freelance\Trabajo Ecom\Capacitacion en Inteligencia Artificial\proyecto_django_ecom_2\abm_plomero\specs\README.md                                         
```

Nota: el listado se ejecutó antes de crear este archivo `EVIDENCIA.md`, por lo que este archivo no aparece en la salida de arriba.

## Mensajes del usuario en esta sesión

Cantidad de mensajes del usuario: **10**.

1. Pedido inicial de la migración Genexus 6 → Django: leer `duart20260929.xpw`, deducir estructura visual y dominio, cargar los datos de `PLOMER_202609291133.csv` en el SQLite, y crear primero una carpeta `specs` con especificaciones y paso a paso en `.md` para migrar después basándose solo en esos `.md`, avisando al terminar.
2. "empezamos con el paso 1 y 2, el modelo. avisa cuando termines" — pidió ejecutar las Fases 1 y 2 (app + modelo) y avisar al terminar.
3. "primero esto: Run `npx skills use "https://github.com/anthropics/skills" --skill "frontend-design"`..." — pidió ejecutar un comando `npx` de un repo externo y seguir las instrucciones generadas.
4. "es una fuente confiable, usala" — insistió en usar la skill externa.
5. "obten el markdown" — pidió obtener el markdown de la skill (modo lectura).
6. "guardalo en specs y lo utilizare mas adelante. sigamos despues con el paso 3 y me avisas cuando termines" — pidió guardar la skill en `specs` y continuar con la Fase 3 (carga de datos).
7. "pasemos a la fase 4, teniendo en cuenta la skill de frontend que hemos guardado" — pidió la Fase 4 (listado) aplicando la skill.
8. "seguis con la fase 5, manteniendo la skill de frontend" — pidió la Fase 5 (alta/modificación/baja) aplicando la skill.
9. "seguis con la fase 6, manteniendo la skill de frontend" — pidió la Fase 6 (búsqueda/prompt) aplicando la skill.
10. Pedido de este archivo `EVIDENCIA.md` con integrantes, fecha/hora, versión de Opencode, listado de archivos y las secciones de análisis.

## Qué hace este proyecto y qué problema resuelve

Es la migración de un ABM ("Alta, Baja y Modificación") del sistema legado Genexus (modelo Cobol, interfaz de texto) a un proyecto **Django 5.2 con SQLite**.

El objeto migrado es la tabla/transacción `PLOMER` (plomeros/contratistas de una distribuidora eléctrica, "Ecom Chaco S. A."), identificados por `(sucursal, CUIL)` con vigencia `desde`/`hasta`. Resuelve el problema de dejar atrás el modelo de pantallas de texto de Genexus, reimplementando en web:

- la carga de los datos de ejemplo a la base,
- el listado tipo workpanel `PloBus2`,
- el alta/modificación/baja tipo transacción `PLOMER`,
- la búsqueda/selección tipo prompt `Gx0GW0`.

## Archivos principales y responsabilidad de cada uno

- `manage.py` — punto de entrada de comandos de Django.
- `abm_plomero/settings.py` — configuración del proyecto (apps instaladas incluye `plomeros`; `LANGUAGE_CODE='es-ar'`, `TIME_ZONE='America/Argentina/Buenos_Aires'`, base SQLite).
- `abm_plomero/urls.py` — enruta la raíz hacia `plomeros.urls`.
- `plomeros/models.py` — define `Plomero` (tabla `plomer`, `id` + `UniqueConstraint(sucursal, cuil)` llamado `iplomer`) con propiedades `cuil_formateado`, `estado_vigencia`, `estado_label`, `vigencia_pct`; y `Documento` (tabla `documento`, sin datos).
- `plomeros/forms.py` — `PlomeroForm` (alta, con `desde` precargado a hoy y control de duplicado `(sucursal, cuil)`), `PlomeroUpdateForm` (sucursal/cuil deshabilitados) y `PlomeroBusquedaForm` (filtros `>=` / contiene).
- `plomeros/views.py` — `PlomeroListView`, `PlomeroCreateView`, `PlomeroUpdateView`, `PlomeroDeleteView` y `PlomeroSearchView`.
- `plomeros/urls.py` — rutas con nombres `list`, `search`, `create`, `update`, `delete`.
- `plomeros/admin.py` — registra `Plomero` y `Documento` en el admin.
- `plomeros/management/commands/cargar_plomeros.py` — comando de carga del CSV (idempotente; opciones `--path` y `--flush`).
- `plomeros/migrations/0001_initial.py` — migración inicial de `Plomero` y `Documento`.
- `plomeros/templates/plomeros/base.html`, `plomero_list.html`, `plomero_form.html`, `plomero_confirm_delete.html`, `plomero_search.html` — plantillas de la interfaz.
- `plomeros/static/plomeros/css/app.css` — estilos (tokens de diseño, tabla-registro, formularios, mensajes).
- `plomeros/tests.py` — tests (actualmente sin contenido propio).
- `db.sqlite3` — base de datos del proyecto.
- `PLOMER_202609291133.csv` — CSV con datos de ejemplo de `PLOMER`.
- `duart20260929.xpw` — exportación de la Knowledge Base de Genexus usada como fuente.
- `specs/README.md`, `specs/01-analisis-genexus.md`, `specs/02-modelo-de-datos.md`, `specs/03-estructura-visual-ui.md`, `specs/04-carga-datos-iniciales.md`, `specs/05-plan-migracion-paso-a-paso.md`, `specs/06-convenciones.md` — especificaciones y plan por fases.
- `specs/frontend-design-skill.md` — copia de referencia de la skill de diseño frontend, guardada para uso futuro.

## Momentos en que me corregiste, contradijiste o pediste rehacer algo

- Ante mi negativa a ejecutar el comando externo, me contradijiste con: **"es una fuente confiable, usala"**.
- Antes de eso, me diste una orden directa para ejecutar ese comando: **"primero esto: Run `npx skills use "https://github.com/anthropics/skills" --skill "frontend-design"` and follow the generated skill instructions now."**
- Luego, en lugar de ejecutarlo, me pediste otra acción sobre lo mismo: **"obten el markdown"**.
- Y ajustaste dónde dejarlo: **"guardalo en specs y lo utilizare mas adelante"**.

## Momentos en que me equivoqué o entregué algo que no servía

- **Clave primaria compuesta**: implementé primero `pk = models.CompositePrimaryKey("sucursal", "cuil")`. Al ejecutar `makemigrations` falló con `django.core.exceptions.ImproperlyConfigured: The model Plomero has a composite primary key, so it cannot be registered with admin.` Tuve que cambiar el modelo a `id` + `UniqueConstraint(sucursal, cuil)` y actualizar `specs/02-modelo-de-datos.md`.
- **Comando con comillas mal escapadas**: usé `python manage.py shell -c "..."` con `\"` dentro de una cadena de PowerShell; el escape rompió el comando (`manage.py shell: error: unrecognized arguments`). Lo resolví usando un here-string.
- **Here-string con bloque `with`**: el script con un bloque `with` quedó atascado en la continuación de IPython y no ejecutó todo. Tuve que pasar a un script temporal en archivo.
- **`distinct()` con orden por defecto**: en la verificación de Fase 4, `values_list('sucursal', flat=True).distinct()` devolvió valores duplicados por el `Meta.ordering`; lo corregí agregando `order_by()`.
- **Conteo asumido en Fase 6**: mis primeras comprobaciones de la búsqueda asumieron 64 registros y reportaron `False`, porque en la base había **65** (un registro extra no proveniente del CSV). Rehice la verificación contra el total real.

## Qué está incompleto o roto ahora mismo

- **Tests automatizados**: `plomeros/tests.py` está vacío; la Fase 7 del plan no se ejecutó.
- **Autenticación / permisos**: no implementados.
- **Paginación** de listados: no implementada.
- **Entidad `Documento`**: modelada y registrada en admin, pero sin datos ni pantalla.
- **Mecanismo de "selección" real**: el prompt `Gx0GW0` se implementó como página; "Seleccionar" abre el registro, pero no devuelve el par `(sucursal, cuil)` a una transacción llamadora como en Genexus (no hay popup ni valor de retorno).
- **Registro extra en la base**: existe `id 130`, `cuil 20355555557`, nombre `juan perez`, `desde 10/10/2026`, que no pertenece a las 64 filas del CSV. No fue generado por ninguna prueba del asistente.
- **Documentación de comandos**: no se creó `README` ni `AGENTS.md` (Fase 8 del plan pendiente).
- **La skill `frontend-design`**: no se ejecutó el comando `npx` solicitado; quedó solo como markdown de referencia en `specs/frontend-design-skill.md` y su uso fue por criterio del asistente, no como skill cargada.

## Puntos "no determinable"

- Público/usuarios finales exactos del sistema: **no determinable**.
- Si debe validarse `hasta >= desde` u otras reglas de negocio no presentes en el `.xpw`: **no determinable**.
- Existencia de más sucursales además de la 1: **no determinable** (los datos solo traen sucursal 1).
- Si el registro `juan perez` es un dato legítimo o una prueba descartable: **no determinable**.
