# Documento de pruebas del componente
## Actividad 4 – Métodos de aprendizaje no supervisado

### 1. Objetivo
Verificar la carga de los datos, la ejecución del algoritmo K-Means, la generación de resultados y la creación de la gráfica.

### 2. Entorno de ejecución
- Sistema operativo: Windows.
- Python: 3.12.3.
- pandas: 3.0.6.
- scikit-learn: 1.9.1.
- matplotlib: 3.8.4.

### 3. Casos de prueba

| ID | Prueba | Resultado esperado | Resultado observado | Estado |
|---|---|---|---|---|
| PR-01 | Cargar el CSV | Leer los registros sin errores. | Se cargaron 36 registros. | Aprobada |
| PR-02 | Validar variables | Detectar valores vacíos en las variables del modelo. | La ejecución continuó sin activar el error de valores vacíos. | Aprobada |
| PR-03 | Entrenar K-Means | Asignar cada registro a uno de tres grupos. | Se generaron tres grupos. | Aprobada |
| PR-04 | Resumir grupos | Calcular promedios por grupo. | Se generó `resumen_grupos.csv`. | Aprobada |
| PR-05 | Evaluar agrupamiento | Calcular la puntuación de silueta. | Se obtuvo 0,5301. | Aprobada |
| PR-06 | Guardar resultados | Crear un CSV con el grupo asignado a cada trayecto. | Se generó `resultados_agrupamiento.csv`. | Aprobada |
| PR-07 | Generar gráfica | Guardar una visualización del agrupamiento. | Se generó `grafica_agrupamiento.png`. | Aprobada |

### 4. Resultados cuantitativos
- Registros procesados: 36.
- Grupo 1: 13 trayectos.
- Grupo 2: 11 trayectos.
- Grupo 3: 12 trayectos.
- Puntuación de silueta: 0,5301.

### 5. Análisis
La ejecución finalizó correctamente y produjo los archivos previstos. La puntuación de silueta de 0,5301 sugiere una separación y cohesión moderadas para esta muestra concreta. La interpretación debe limitarse a los datos sintéticos utilizados y no generalizarse al funcionamiento real de TransMilenio.

### 6. Evidencias
La evidencia de ejecución puede consultarse en:
- `resultados_agrupamiento.csv`
- `resumen_grupos.csv`
- `grafica_agrupamiento.png`

Se recomienda incluir capturas de la terminal donde se observa la ejecución y de la gráfica generada.

### 7. Limitaciones
Las pruebas verifican el comportamiento del programa con el dataset disponible. No demuestran que los grupos representen trayectos reales ni que el modelo esté validado para decisiones operativas.
