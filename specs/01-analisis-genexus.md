# 01 - Análisis del archivo Genexus (`duart20260929.xpw`)

## 1. Cabecera del Knowledge Base

```
Model=  2: Cobol (Production)
objetos para IA
:KMW
  MajorVersion=1
  MinorVersion=5
  Path=z:\KBs_3107\kb3107RealReal
```

- Modelo de generación: **Cobol (Production)** → interfaz de texto (green screen).
- KB versión 1.5.

## 2. Objetos contenidos

| Objeto | Tipo | Nombre | Descripción | Rol |
|--------|------|--------|-------------|-----|
| `Gx0GW0` / `WGx0GW0` | Prompt | Lista de Selección PLOMER | Búsqueda y selección de plomeros | Selección |
| `PloBus2` | WorkPanel | PloBus2 | ABM de plomeros | Mantenimiento |
| `PLOMER` | Transaction | PLOMER | Transacción de plomeros | CRUD |
| `PLOMER` | Table | PLOMER | Tabla física Id = 608 | Persistencia |
| `Docu_codigo`, `Docu_nombre` | Atributos externos | — | Tipos de Documentos | Referenciados (UI) |

Objetos externos invocados (no incluidos en el `.xpw`):

- `TPLOMER` → llamado por `PloBus2` con modos `INS`, `UPD`, `DLT` (realiza el ABM).
- `PSucu` → llamado por `PLOMER` Event `Start` para obtener sucursal y descripción.

## 3. Atributos y dominio (tipos Genexus)

Atributos propios de la tabla `PLOMER`:

| Id | Atributo GX | Nombre lógico | Tipo GX | Longitud | Picture | Dominio / observación |
|----|-------------|---------------|---------|----------|---------|-----------------------|
| 5163 | `PloSucu` | Sucursal | Numeric | 2 | `Z9` | Código de sucursal (0–99) |
| 5164 | `PloCod` | Código / **CUIL** | Numeric | 11 | `ZZZZZZZZZZ9` | Identificador del plomero (CUIL) |
| 5165 | `PloNom` | Apellido y nombre | Character | 20 | — | Texto |
| 5189 | `PloDes` | Vigencia **Desde** | Date | 8 | — | Fecha |
| 5190 | `PloHas` | Vigencia **Hasta** | Date | 8 | — | Fecha |

Atributos de la tabla secundaria *Tipos de Documentos* (referenciados en la UI, sin transacción definida en el `.xpw`):

| Id | Atributo GX | Tipo | Longitud | Picture |
|----|-------------|------|----------|---------|
| 7 | `Docu_codigo` | Numeric | 2 | `Z9` |
| 8 | `Docu_nombre` | Character | (desconocida) | — |

> **Dominio (GX):** el `.xpw` **no define dominios personalizados** (`:Domain`). Los atributos usan tipos base.
> Se usa `BasedOn` únicamente para variables (`V5163→PloSucu`, `V5164→PloCod`, etc.).

## 4. Transacción `PLOMER`

### 4.1 Estructura

```
PloSucu*      (clave)
PloCod*       (clave)
PloNom
PloDes
PloHas
```

### 4.2 Reglas (Rules)

```
parm(&opera ,&sucu ,&PloCod ,&Mode ) ;
noaccept(&SucDescri ) ;
noaccept(PloSucu ) ;
PloSucu = &Sucu ;
PloCod = &PloCod IF &Mode = 'DLT' ;
PloCod = &PloCod IF &Mode = 'UPD' ;
PloCod = &PloCod IF &Mode = 'DSP' ;
color('X,X' ,PloSucu ) ;
PloDes = &Today IF &Mode = 'INS' ;
```

Interpretación:

- La transacción recibe como parámetro el **modo** (`INS`/`UPD`/`DLT`/`DSP`), la **sucursal** y el **código**.
- `PloSucu` no es aceptada del usuario (se fija por parámetro `&sucu`).
- `PloCod` no se acepta cuando el modo es `DLT`/`UPD`/`DSP` (solo editable en alta).
- En modo `INS`, `PloDes` toma la fecha actual (`&Today`) como valor por defecto.
- `SucDescri` es solo lectura (descripción de sucursal).

### 4.3 Eventos (Events)

```
Event Start
  call( PSucu, &sucu ,&SucDescri )
EndEvent
```

- Al iniciar, se invoca `PSucu` para resolver la descripción de la sucursal.

### 4.4 Tabla / Índices

```
Table PLOMER (Id=608)
  Key = PloSucu
  Key = PloCod
  Index IPLOMER  Type=System  UniqueDuplicate=Unique  (PloSucu, PloCod)
```

→ **Clave primaria compuesta**: `(PloSucu, PloCod)` con índice **único**.

## 5. WorkPanel `PloBus2` (ABM)

Descripción: `PloBus2`. Contiene **dos formularios**:

- **FormId=1** (`FormClass=Graphic`): bloque "Tipos de Documentos" con grilla `Op, Docu_codigo, Docu_nombre`.
  Este bloque es **inconsistente** con la lógica de eventos (que trabaja sobre `PloCod`), por lo que se considera
  un remanente de plantilla heredada. **No es el formulario canónico.**
- **FormId=2** (`FormClass=Text`, modo texto/dato): bloque **"Plomeros"**, que es el ABM real.

### 5.1 Formulario canónico (FormId=2, "Plomeros")

Grilla principal (`SubFile`) con columnas:

| Columna | Atributo | Ancho |
|---------|----------|-------|
| `Op` | variable de operación | 32 |
| `PloCod` | CUIL | 96 |
| `PloNom` | Apellido y nombre | 168 |
| `PloDes` | Vigencia desde | 72 |
| `PloHas` | Vigencia hasta | 64 |

Campos de contexto: `PloSucu` (sucursal, solo lectura), `Pgmname`, `Today`, `Time`.
Etiquetas visibles: `Op.`, `CUIL`, `Apellido y Nombre`, `Vigencia`, `Desde`, `Hasta`, `F6-Alta`, `#CC`.

### 5.2 Reglas

```
parm(&opera ,&Sucu ,&PloCod ,&PloNom ) ;
color('X,X' ,PloSucu ) ;
```

### 5.3 Eventos

```
// especificado #CC 01/04/19 - SM

event Enter
    For each line
        if &Op = '2'
            &Mode = 'UPD'
            call(TPLOMER ,&opera ,&sucu ,PloCod ,&Mode )
            &Op=' '
            REFRESH KEEP
        endif
        if &Op = '3'
            &Mode = 'DLT'
            call(TPLOMER ,&opera ,&sucu ,PloCod ,&Mode )
            &Op=' '
            REFRESH KEEP
        endif
    endfor
endevent

Event 'F6-Alta' 06
    &Mode = 'INS'
    call(TPLOMER ,&opera ,&sucu ,&PloCod ,&Mode )
    &Op=' '
    REFRESH KEEP
Endevent
```

Comportamiento:

- **Enter**: recorre las líneas de la grilla; si `Op = '2'` → modificar (`UPD`); si `Op = '3'` → baja (`DLT`).
- **F6**: alta (`INS`).
- Tras cada operación se refresca la grilla (`REFRESH KEEP`).

## 6. Prompt `Gx0GW0` (*Lista de Selección PLOMER*)

### 6.1 Reglas

```
parm(&V5163 ,&V5164 ) ;
order(PloSucu ,PloCod ) ;
```

### 6.2 Condiciones de filtro

```
PloSucu >= &C5163 ;
PloCod  >= &C5164 ;
PloNom  .LIKE. &C5165 ;
PloDes  >= &C5189 ;
PloHas  >= &C5190 ;
```

### 6.3 Grilla de resultados

Columnas: `PloSucu`, `PloCod`, `PloNom`, `PloDes`, `PloHas` (anchos 64, 96, 168, 72, 64).

### 6.4 Evento

```
//Especificado 11/04/2019 - KV

Event Enter
    &V5163 = PloSucu
    &V5164 = PloCod
    Return
EndEvent
```

Devuelve la sucursal y el código del registro seleccionado.

## 7. Estructura visual (resumen)

- Interfaz **modo texto** (Cobol), fuentes `Courier New` tamaño 9/10, colores:
  - Fondo `Black`, texto `Lime`, títulos en `Blue`/`Fuchsia`.
  - Grillas con pen/line en `Lime` sobre `Black`.
- Layout por coordenadas `left/top/right/bottom` (equivalente a celdas de pantalla).
- El ABM se compone de: cabecera (programa, fecha/hora, sucursal), grilla central y línea de opciones.
- El prompt es una ventana de selección con grilla y filtros.

Ver detalle en [03-estructura-visual-ui.md](03-estructura-visual-ui.md).

## 8. Observaciones / riesgos detectados

1. **FormId=1 del WorkPanel** referencia `Docu_*` (Tipos de Documentos) y no la lógica de plomeros → remanente; migrar solo FormId=2.
2. Dependencias externas `TPLOMER` y `PSucu` no incluidas: se **absorben** en los views/services de Django.
3. `PloCod` corresponde al **CUIL** (etiqueta "CUIL"/"Cuil" en la UI, valores de 11 dígitos).
4. Formato de fecha Genexus/CSV es `YYYYMMDD`; requiere conversión a `date`.
5. Codificación: el `.xpw` muestra caracteres `�` (mojibake, probablemente latin-1/cp1252); el CSV debe leerse como **UTF-8**.
