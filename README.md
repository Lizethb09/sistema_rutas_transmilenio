# Sistema Inteligente de Búsqueda de Rutas para TransMilenio - Bogotá

## Descripción

Este proyecto implementa un sistema inteligente de búsqueda de rutas para un modelo académico simplificado del sistema TransMilenio de Bogotá.

El sistema utiliza una base de conocimiento representada mediante un grafo de estaciones y conexiones. A partir de una estación de origen y una estación de destino, el algoritmo A* realiza una búsqueda para encontrar una ruta entre ambos puntos.

El proyecto fue desarrollado como parte de la actividad académica de Inteligencia Artificial de la Corporación Universitaria Iberoamericana.

## Objetivo

Desarrollar un sistema inteligente basado en conocimiento que permita encontrar una ruta entre dos estaciones utilizando una estrategia de búsqueda heurística.

## Tecnologías utilizadas

* Python 3.
* Visual Studio Code.
* Algoritmo de búsqueda A*.
* Estructuras de datos tipo diccionario.
* Distancia Manhattan como función heurística.

## Representación del conocimiento

La base de conocimiento se representa mediante un conjunto de estaciones y sus conexiones.

Cada estación contiene las estaciones a las que puede conectarse y un costo interno utilizado por el algoritmo de búsqueda.

Las reglas lógicas implementadas permiten:

1. Determinar si existe una conexión entre dos estaciones.
2. Obtener las estaciones vecinas de una estación.
3. Obtener el costo interno de una conexión.

## Algoritmo de búsqueda

El sistema utiliza el algoritmo A*.

La función de evaluación utilizada es:

f(n) = g(n) + h(n)

Donde:

* g(n) representa el costo acumulado desde la estación de origen hasta la estación actual.
* h(n) representa una estimación del costo restante hasta el destino.
* f(n) representa el valor utilizado para seleccionar la siguiente estación que será explorada.

La heurística utilizada corresponde a la distancia Manhattan:

h(n) = |x1 - x2| + |y1 - y2|

## Tarifa del sistema

El sistema muestra una tarifa de referencia de $3.550 COP correspondiente a la tarifa del sistema TransMilenio para 2026.

Esta tarifa se muestra como el precio del viaje y no se utiliza como costo de cada conexión dentro del algoritmo A*.

Los costos internos utilizados por A* corresponden a valores del modelo académico y se utilizan únicamente para realizar la búsqueda de rutas.

## Estaciones incluidas

El modelo académico utilizado en este proyecto contiene las siguientes estaciones:

1. Portal Norte
2. Calle 100
3. NQS Calle 75
4. Calle 63
5. Universidad Nacional
6. Calle 26
7. Museo Nacional
8. San Diego
9. Universidades

## Ejecución del proyecto

Para ejecutar el sistema es necesario tener Python instalado.

Desde la carpeta del proyecto se ejecuta el siguiente comando:

```bash
python main.py
```

El sistema mostrará las estaciones disponibles y solicitará al usuario seleccionar:

1. La estación de origen.
2. La estación de destino.

Posteriormente, el algoritmo A* realizará la búsqueda y mostrará la ruta encontrada, el número de estaciones, el costo interno de búsqueda y la tarifa del viaje.

## Ejemplo de ejecución

Un ejemplo de búsqueda es:

Origen:

Portal Norte

Destino:

Universidades

El sistema puede encontrar una ruta como:

Portal Norte → Calle 100 → NQS Calle 75 → Universidad Nacional → Calle 26 → Museo Nacional → Universidades

## Validaciones

El sistema incluye validaciones para:

* Números de estación fuera del rango permitido.
* Estaciones de origen y destino.
* Selección de la misma estación como origen y destino.

## Pruebas

El funcionamiento del sistema fue comprobado mediante diferentes casos de prueba:

* Búsqueda de una ruta válida.
* Búsqueda de una ruta en sentido contrario.
* Búsqueda de una ruta corta.
* Selección de la misma estación como origen y destino.
* Ingreso de un número de estación inválido.

Los resultados de las pruebas se encuentran documentados en el archivo correspondiente dentro del proyecto.

## Estructura del proyecto

```text
sistema_rutas_transmilenio/
│
├── main.py
├── README.md
└── pruebas/
```

## Autora

Lizeth Valentina Benítez

Corporación Universitaria Iberoamericana

Programa de Ingeniería de Software

Actividad de Inteligencia Artificial
