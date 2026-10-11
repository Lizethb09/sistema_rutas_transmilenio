# Descripción del conjunto de datos
## Actividad 3 - Métodos de aprendizaje supervisado

**Proyecto:** Sistema Inteligente de Búsqueda de Rutas para TransMilenio - Bogotá  
**Estudiante:** Lizeth Valentina Benítez  
**Asignatura:** Inteligencia Artificial  
**Institución:** Corporación Universitaria Iberoamericana (IBERO)

## 1. Objetivo

Describir el conjunto de datos utilizado para entrenar y evaluar un modelo de aprendizaje supervisado que clasifica trayectos del sistema de transporte masivo en las categorías corto, medio y largo.

## 2. Fuente de los datos

El archivo utilizado es `dataset_transmilenio.csv`, ubicado en la carpeta `datos` de la Actividad 3.

El conjunto de datos fue construido sintéticamente con fines académicos, debido a que esta implementación utiliza una muestra propia. No corresponde a una descarga de una base de datos oficial ni representa mediciones reales de la operación de TransMilenio.

## 3. Estructura

El archivo contiene 36 registros válidos y seis columnas:

| Campo | Descripción | Tipo de dato |
|---|---|---|
| origen | Estación de origen del trayecto | Texto |
| destino | Estación de destino del trayecto | Texto |
| numero_estaciones | Número de estaciones considerado para el trayecto | Numérico entero |
| costo_interno | Costo numérico interno asignado al trayecto para el ejercicio | Numérico |
| transbordos | Número de transbordos considerados | Numérico entero |
| categoria_trayecto | Categoría objetivo: corto, medio o largo | Categórico |

El campo `costo_interno` es una variable del modelo y no debe interpretarse como el precio real del pasaje.

## 4. Variables del modelo

### Variables de entrada

El modelo utiliza las siguientes características:

- `numero_estaciones`
- `costo_interno`
- `transbordos`

### Variable objetivo

La variable que el modelo aprende a predecir es `categoria_trayecto`, con tres clases: `corto`, `medio` y `largo`.

Los campos `origen` y `destino` se conservan como información descriptiva del trayecto, pero no se utilizan directamente como características en el modelo actual.

## 5. Distribución de las categorías

Según la ejecución del programa, los 36 registros se distribuyen así:

| Categoría | Cantidad |
|---|---:|
| corto | 13 |
| medio | 14 |
| largo | 9 |
| **Total** | **36** |

## 6. Preparación y uso de los datos

El programa carga el archivo CSV mediante la biblioteca pandas. Posteriormente utiliza las tres características numéricas para entrenar un clasificador supervisado con scikit-learn.

La ejecución registrada divide los datos en 27 registros de entrenamiento y 9 registros de prueba.

## 7. Limitaciones

- Los datos son sintéticos y se crearon para demostrar el funcionamiento del aprendizaje supervisado.
- La distribución de las categorías puede influir en los resultados.
- La exactitud obtenida en la prueba no demuestra el desempeño con datos reales.
- Para una aplicación real se necesitarían datos confiables y actualizados sobre estaciones, recorridos, tiempos, costos y transbordos.

## 8. Conclusión

El conjunto de datos permite desarrollar una demostración académica de clasificación supervisada aplicada a trayectos de TransMilenio. Su estructura facilita relacionar características numéricas con una categoría objetivo y evaluar el resultado mediante métricas de clasificación. Los resultados deben interpretarse dentro de los límites de una muestra sintética.
