# Especificaciones de Migración Genexus → Django

Sistema origen: **Genexus 6 / 9 (Model = 2: Cobol Production)**
Sistema destino: **Django 6.1 (SQLite)**

## Objetivo

Migrar el módulo **ABM de Plomeros** (`PLOMER`) de Genexus a Django, incluyendo:

- Estructura visual (pantallas de texto / workpanel / prompt).
- Dominio y modelo de datos.
- Carga de los datos de ejemplo del archivo `PLOMER_202609291133.csv` a la base SQLite del proyecto.

## Alcance de esta etapa

Esta carpeta contiene **solamente especificaciones**. No se implementa código de la migración todavía.
Una vez aprobadas, el proyecto se construye basándose únicamente en estos documentos.

## Índice

| Documento | Contenido |
|-----------|-----------|
| [01-analisis-genexus.md](01-analisis-genexus.md) | Lectura del `.xpw`: objetos, atributos, dominio, eventos, reglas y estructura visual. |
| [02-modelo-de-datos.md](02-modelo-de-datos.md) | Entidades, tipos, claves y mapeo al modelo Django + DDL SQL. |
| [03-estructura-visual-ui.md](03-estructura-visual-ui.md) | Layout de pantallas Genexus y su equivalente web. |
| [04-carga-datos-iniciales.md](04-carga-datos-iniciales.md) | Análisis del CSV y estrategia de carga a SQLite. |
| [05-plan-migracion-paso-a-paso.md](05-plan-migracion-paso-a-paso.md) | Plan de trabajo por fases con pasos concretos. |
| [06-convenciones.md](06-convenciones.md) | Convenciones de código, comandos y criterios de aceptación. |

## Resumen ejecutivo del origen

- **Transacción** `PLOMER` (descripción: *PLOMEROS*) con claves compuestas `PloSucu + PloCod`.
- **WorkPanel** `PloBus2` que opera el ABM (Alta / Modificación / Baja) sobre plomeros.
- **Prompt** `Gx0GW0` (*Lista de Selección PLOMER*) para búsqueda/selección.
- **Tabla física** `PLOMER` (Id 608) con índice único `IPLOMER (PloSucu, PloCod)`.
- 5 atributos principales: sucursal, CUIL, nombre, vigencia desde, vigencia hasta.
- Datos de ejemplo: 64 registros en `PLOMER_202609291133.csv`.

## Archivos fuente de referencia

- `duart20260929.xpw` — knowledge base exportada de Genexus.
- `PLOMER_202609291133.csv` — datos de ejemplo de la tabla PLOMER.
- Proyecto Django existente en la raíz (`manage.py`, `abm_plomero/settings.py`, `db.sqlite3`).
