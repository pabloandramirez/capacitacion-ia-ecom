# 03 - Estructura visual y mapeo a UI web

## 1. Características de la UI origen

- Tipo: **modo texto** (generación Cobol), sin gráficos web.
- Fuente base: `Courier New`, tamaños 9 y 10; títulos en negrita/subrayado.
- Paleta:
  - Frame fondo `Black`, texto `Lime`.
  - Títulos: `Blue` (ej. "Plomeros", "Tabla de plomeros") y `Fuchsia` (mensajes de opciones / "F6-Alta").
  - Grillas: borde/pen `Lime` sobre `Black`; fondo de frame secundario `Silver`.
- Posicionamiento absoluto por `left/top/right/bottom` (celdas de pantalla de texto).
- Navegación por teclado: `Enter` (procesar), `F6` (alta), códigos de operación `1/2/3`.

## 2. Pantalla 1 — WorkPanel `PloBus2` (FormId=2, "Plomeros")

### 2.1 Layout lógico (bloques)

```
Fila superior:
  [Pgmname] (#CC)                          [Today] [Time]
  Plomeros                                   (título azul)

Barra de opciones:
  Opc.:2-Modifica   3-Baja            F6-Alta (fucsia)

Cabecera de grilla:
  Op.        CUIL                Apellido y Nombre        Vigencia
                                                          Desde    Hasta
  ----------------------------------------------------------------
  | Op | PloCod | PloNom | PloDes | PloHas |              (SubFile)

Línea inferior:
  [Sucursal / PloSucu]
```

### 2.2 Elementos y su equivalente web

| Elemento GX | Tipo | Equivalente web |
|-------------|------|-----------------|
| `Pgmname` | Edit | Texto de cabecera (nombre de programa) |
| `Today` / `Time` | Edit | Fecha/hora actual en cabecera |
| `PloSucu` | Edit | Selector/campo de sucursal (solo lectura en contexto) |
| SubFile "Plomeros" | Grilla | Tabla HTML con columnas `Op`, CUIL, Nombre, Desde, Hasta |
| `Op` | columna editable | Campo de operación por fila (`2`=modificar, `3`=baja) |
| Textos "Op.", "CUIL", etc. | Labels | Encabezados de tabla |
| `F6-Alta` | Evento de teclado | Botón **"Alta"** |
| `Enter` | Evento | Botón **"Procesar"** / acción de fila |

### 2.3 Interacciones

- **Alta**: botón → formulario de alta (precarga `sucursal` del contexto y `desde = hoy`).
- **Modificación**: botón/acción por fila → formulario de edición (CUIL bloqueado).
- **Baja**: acción por fila con confirmación.
- **Refrescar**: recarga de la grilla tras cada operación.

## 3. Pantalla 2 — Prompt `Gx0GW0` (Lista de Selección PLOMER)

### 3.1 Layout lógico

```
Pgmdesc (título/subrayado)

PloSucu  [PloSucu]      PloCod [PloCod]
PloNom   [PloNom]
PloDes   [PloDes]       PloHas [PloHas]

  ------------------------------------------------------------
  | PloSucu | PloCod | PloNom | PloDes | PloHas |   (SubFile)
  ------------------------------------------------------------
```

### 3.2 Equivalente web

- Formulario de **búsqueda/filtros** con los 5 campos (condiciones `>=` para sucursal/código/fechas y `LIKE` para nombre).
- Grilla de resultados ordenada por `(PloSucu, PloCod)`.
- Acción de selección de fila → devuelve `(sucursal, cuil)`.
- Se implementa como ventana modal/popup (propiedad GX `WNDPOP=CMP`, `popup('Y')`).

## 4. Pantalla 3 — Transacción `PLOMER` (formulario de edición)

### 4.1 Layout lógico

```
Pgmname    [Pgmname]                    Tabla de plomeros
                                        [Today] [Time]
Operador:  [Opera]      Cuil [PloCod edit]
---------------------------------------------------------
[PloSucu edit]          Apellido y nombres [PloNom edit]
                        Vigencia   Desde [PloDes]  Hasta [PloHas]
---------------------------------------------------------
Ecom Chaco S. A.
```

### 4.2 Equivalente web

- Formulario de detalle/edición con campos:
  - `sucursal` (no editable en transacción),
  - `cuil` (editable solo en alta),
  - `nombre`,
  - `desde` (precargado con hoy en alta),
  - `hasta`.
- `SucDescri` (descripción de sucursal) solo lectura, resuelto por `PSucu`.
- Botones Guardar/Cancelar; mensajes de confirmación/error.

## 5. Mapeo de colores y estilo

| Origen | Propósito | Web propuesto |
|--------|-----------|---------------|
| Fondo negro / texto limón | Frames y grillas | Tema oscuro o neutral (a definir); priorizar legibilidad |
| Azul | Títulos | Encabezados `h1/h2` |
| Fucsia | Mensajes/opciones | Texto de ayuda / badges |
| Courier New 9/10 | Tipografía general | Fuente monoespaciada solo si se desea fidelidad |

> Nota: no es requisito replicar los colores exactos de la terminal; se documentan para preservar semántica (títulos, ayudas, estados).

## 6. Flujo de navegación

```
Lista de Plomeros (PloBus2)
   ├─ Alta (F6) ─────────► Formulario PLOMER (modo INS)
   ├─ Op=2 (Modificar) ──► Formulario PLOMER (modo UPD)
   ├─ Op=3 (Baja) ───────► Confirmación / Formulario PLOMER (modo DLT)
   └─ Buscar ────────────► Prompt Gx0GW0 → selección (sucursal, cuil)
```

## 7. Consideraciones de usabilidad web

- Mantener el orden de columnas de la grilla origen.
- Mantener el orden de ordenamiento `(sucursal, cuil)`.
- Confirmar bajas (no existía confirmación explícita en GX; agregarla mejora seguridad).
- Paginación de la grilla (en GX se maneja con la variable `Page`).
