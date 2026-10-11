# Documento de pruebas del modelo supervisado

## Actividad 3 - Métodos de aprendizaje supervisado

**Proyecto:** Sistema Inteligente de Búsqueda de Rutas para TransMilenio - Bogotá  
**Estudiante:** Lizeth Valentina Benítez  
**Asignatura:** Inteligencia Artificial  
**Institución:** Corporación Universitaria Iberoamericana (IBERO)

## 1. Objetivo de las pruebas

Verificar la ejecución del programa de aprendizaje supervisado, la carga del conjunto de datos, el entrenamiento del clasificador, la evaluación de sus resultados y la generación de una predicción de ejemplo.

## 2. Entorno de ejecución

- Lenguaje de programación: Python.
- Biblioteca para manipulación de datos: pandas.
- Biblioteca de aprendizaje automático: scikit-learn.
- Archivo de datos: `dataset_transmilenio.csv`.
- Programa evaluado: `modelo_supervisado.py`.

## 3. Casos de prueba

| Código | Prueba | Resultado observado | Estado |
|---|---|---|---|
| PR-01 | Cargar el conjunto de datos CSV | Se cargaron 36 registros válidos. | Aprobada |
| PR-02 | Identificar las categorías | Se identificaron las categorías corto, medio y largo. | Aprobada |
| PR-03 | Dividir los datos | Se utilizaron 27 registros para entrenamiento y 9 para prueba. | Aprobada |
| PR-04 | Entrenar y evaluar el modelo | El programa terminó el entrenamiento y reportó una exactitud del 100 % en los 9 registros de prueba. | Aprobada |
| PR-05 | Generar una predicción | Para el ejemplo de 4 estaciones, costo interno 5 y 1 transbordo, el modelo predijo la categoría medio. | Aprobada |

## 4. Resultados de la evaluación

La ejecución del programa mostró la siguiente distribución del conjunto de datos:

| Categoría | Cantidad de registros |
|---|---:|
| Corto | 13 |
| Medio | 14 |
| Largo | 9 |
| Total | 36 |

La matriz de confusión obtenida fue:

| Categoría real / predicha | Corto | Largo | Medio |
|---|---:|---:|---:|
| Corto | 3 | 0 | 0 |
| Largo | 0 | 2 | 0 |
| Medio | 0 | 0 | 4 |

En esta ejecución, las 9 observaciones de prueba fueron clasificadas correctamente. Por ello, la exactitud reportada fue del 100 %.

## 5. Interpretación de los resultados

Los resultados muestran que el programa ejecuta correctamente el flujo de clasificación supervisada con el conjunto de datos utilizado. La matriz de confusión no presenta errores de clasificación en las 9 observaciones evaluadas.

Sin embargo, este resultado no garantiza una exactitud del 100 % con otros datos ni con recorridos reales de TransMilenio. La muestra utilizada es sintética y tiene fines académicos, por lo que sería necesario evaluar el modelo con datos reales y representativos antes de utilizarlo en una aplicación práctica.

## 6. Conclusión

Las pruebas registradas permiten comprobar la carga de los datos, la preparación del conjunto de entrenamiento y prueba, la evaluación del clasificador y la generación de una predicción. El ejercicio demuestra el funcionamiento básico del aprendizaje supervisado aplicado a la clasificación de trayectos.

