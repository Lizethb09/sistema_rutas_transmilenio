# Descripción de los datos
## Actividad 4 – Métodos de aprendizaje no supervisado

### 1. Nombre del conjunto de datos
dataset_trayectos_no_supervisado.csv

### 2. Objetivo
Representar una muestra de trayectos hipotéticos relacionados con el transporte masivo de Bogotá para explorar agrupaciones mediante el algoritmo K-Means.

### 3. Origen de los datos
El conjunto de datos fue construido de forma sintética con fines académicos. No corresponde a registros oficiales ni a mediciones reales de TransMilenio. Por tanto, sus resultados no deben interpretarse como una descripción validada de la operación real del sistema.

### 4. Tamaño
El dataset contiene 36 registros y cuatro columnas: un identificador y tres variables numéricas utilizadas por el modelo.

### 5. Diccionario de datos

| Campo | Tipo | Descripción |
|---|---|---|
| id_trayecto | Texto | Identificador único del trayecto sintético. |
| numero_estaciones | Entero | Cantidad hipotética de estaciones del trayecto. |
| costo_interno | Numérico | Valor sintético utilizado como variable de comparación; no representa una tarifa oficial en pesos colombianos. |
| transbordos | Entero | Cantidad hipotética de transbordos del trayecto. |

### 6. Preparación de los datos
Se cargaron los datos con pandas y se verificó que existieran registros y que las variables utilizadas no tuvieran valores vacíos. Las tres variables numéricas se estandarizaron mediante StandardScaler antes del entrenamiento para evitar que las diferencias de escala dominaran el agrupamiento.

### 7. Método de aprendizaje no supervisado
Se utilizó K-Means de scikit-learn con tres grupos, `random_state=42` y `n_init=10`. El modelo utiliza las variables `numero_estaciones`, `costo_interno` y `transbordos`. No se proporcionaron etiquetas de categoría como objetivo durante el entrenamiento.

### 8. Resultados obtenidos
Los promedios calculados fueron:

| Grupo | Estaciones promedio | Costo interno promedio | Transbordos promedio | Registros |
|---|---:|---:|---:|---:|
| 1 | 11,77 | 9,85 | 2,15 | 13 |
| 2 | 18,09 | 15,00 | 3,55 | 11 |
| 3 | 5,08 | 4,42 | 0,58 | 12 |

La puntuación de silueta obtenida fue 0,5301. Esta métrica aporta una medida de la cohesión y separación de los grupos para los datos utilizados; no constituye por sí sola una validación definitiva del modelo.

### 9. Archivos relacionados
- `../datos/dataset_trayectos_no_supervisado.csv`: datos de entrada.
- `../modelo_no_supervisado.py`: código fuente del modelo.
- `../pruebas/resultados_agrupamiento.csv`: asignación de cada trayecto a un grupo.
- `../pruebas/resumen_grupos.csv`: características promedio de los grupos.
- `../pruebas/grafica_agrupamiento.png`: visualización de estaciones frente a costo interno.

### 10. Limitaciones
La muestra es pequeña y sintética. El número de grupos se fijó en tres como decisión experimental. Los identificadores de grupo son arbitrarios y pueden cambiar si se modifican los datos o los parámetros. Se recomienda evaluar otros valores de K y, para aplicaciones reales, utilizar datos confiables y representativos del sistema de transporte.
