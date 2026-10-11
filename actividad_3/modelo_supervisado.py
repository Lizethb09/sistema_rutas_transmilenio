
# ============================================
# ACTIVIDAD 5 - INTELIGENCIA ARTIFICIAL
# APRENDIZAJE SUPERVISADO
# SISTEMA DE RUTAS TRANSMILENIO - BOGOTA
# ============================================

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# ============================================
# CONFIGURACION DE RUTAS Y ARCHIVOS
# ============================================

CARPETA_PROYECTO = Path(__file__).resolve().parent
ARCHIVO_DATASET = (
    CARPETA_PROYECTO / "datos" / "dataset_transmilenio.csv"
)


# ============================================
# CARGAR Y VALIDAR EL DATASET
# ============================================

def cargar_dataset():
    """Carga el dataset y verifica las columnas necesarias."""

    if not ARCHIVO_DATASET.exists():
        raise FileNotFoundError(
            f"No se encontro el archivo: {ARCHIVO_DATASET}"
        )

    datos = pd.read_csv(ARCHIVO_DATASET, encoding="utf-8")

    columnas_requeridas = [
        "numero_estaciones",
        "costo_interno",
        "transbordos",
        "categoria_trayecto"
    ]

    faltantes = [
        columna
        for columna in columnas_requeridas
        if columna not in datos.columns
    ]

    if faltantes:
        raise ValueError(
            "Faltan columnas requeridas en el CSV: "
            + ", ".join(faltantes)
        )

    datos = datos[columnas_requeridas].copy()

    datos["numero_estaciones"] = pd.to_numeric(
        datos["numero_estaciones"], errors="coerce"
    )
    datos["costo_interno"] = pd.to_numeric(
        datos["costo_interno"], errors="coerce"
    )
    datos["transbordos"] = pd.to_numeric(
        datos["transbordos"], errors="coerce"
    )

    datos["categoria_trayecto"] = (
        datos["categoria_trayecto"].astype("string").str.strip().str.lower()
    )

    datos = datos.dropna()

    if datos.empty:
        raise ValueError(
            "El dataset no contiene filas validas para entrenar."
        )

    if datos["categoria_trayecto"].nunique() < 2:
        raise ValueError(
            "Se necesitan al menos dos categorias para entrenar."
        )

    return datos


# ============================================
# ENTRENAR Y EVALUAR EL MODELO
# ============================================

def entrenar_y_evaluar(datos):

    # Caracteristicas utilizadas por el modelo.
    # No se usan los nombres de origen y destino para
    # reducir el riesgo de memorizar estaciones concretas.
    caracteristicas = [
        "numero_estaciones",
        "costo_interno",
        "transbordos"
    ]

    X = datos[caracteristicas]
    y = datos["categoria_trayecto"]

    # Se comprueba que cada categoria tenga suficientes
    # ejemplos para aparecer en entrenamiento y prueba.
    conteo_categorias = y.value_counts()

    if len(datos) < 8 or conteo_categorias.min() < 2:
        raise ValueError(
            "El dataset es demasiado pequeno o alguna categoria "
            "tiene menos de dos ejemplos. Agrega mas ejemplos "
            "antes de dividir los datos."
        )

    # Separacion de datos: 75 % entrenamiento y 25 % prueba.
    X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = (
        train_test_split(
            X,
            y,
            test_size=0.25,
            random_state=42,
            stratify=y
        )
    )

    # Creacion del arbol de decision.
    modelo = DecisionTreeClassifier(
        max_depth=3,
        random_state=42
    )

    # Entrenamiento del modelo.
    modelo.fit(X_entrenamiento, y_entrenamiento)

    # Predicciones sobre los datos de prueba.
    predicciones = modelo.predict(X_prueba)

    # ========================================
    # MOSTRAR RESULTADOS
    # ========================================

    print("\n==============================================")
    print(" MODELO SUPERVISADO - TRANSMILENIO")
    print("==============================================")

    print(f"\nArchivo de datos: {ARCHIVO_DATASET.name}")
    print(f"Total de registros validos: {len(datos)}")

    print("\nDistribucion de categorias:")
    print(y.value_counts().to_string())

    print("\nCaracteristicas utilizadas:")
    for caracteristica in caracteristicas:
        print(f"- {caracteristica}")

    print("\nDivision de los datos:")
    print(f"Registros de entrenamiento: {len(X_entrenamiento)}")
    print(f"Registros de prueba: {len(X_prueba)}")

    exactitud = accuracy_score(y_prueba, predicciones)

    print("\nExactitud del modelo:")
    print(f"{exactitud:.2%}")

    print("\nReporte de clasificacion:")
    print(
        classification_report(
            y_prueba,
            predicciones,
            labels=sorted(y.unique()),
            zero_division=0
        )
    )

    etiquetas = sorted(y.unique())

    print("Matriz de confusion:")
    print("Orden de las categorias:", etiquetas)
    print(confusion_matrix(
        y_prueba,
        predicciones,
        labels=etiquetas
    ))

    # ========================================
    # PREDICCION DE UN EJEMPLO NUEVO
    # ========================================

    ejemplo_nuevo = pd.DataFrame(
        [{
            "numero_estaciones": 4,
            "costo_interno": 5,
            "transbordos": 1
        }]
    )

    categoria_predicha = modelo.predict(ejemplo_nuevo)[0]

    print("\n==============================================")
    print(" PREDICCION DE EJEMPLO")
    print("==============================================")

    print("Numero de estaciones: 4")
    print("Costo interno: 5")
    print("Transbordos: 1")
    print(f"Categoria predicha: {categoria_predicha}")

    print("\nNota:")
    print(
        "El dataset contiene ejemplos sinteticos creados "
        "con fines academicos."
    )
    print(
        "Los resultados no representan mediciones reales "
        "del sistema TransMilenio."
    )

    return modelo


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

def main():
    try:
        datos = cargar_dataset()
        entrenar_y_evaluar(datos)

    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        print("\nNo fue posible ejecutar el modelo.")
        print(f"Detalle: {error}")

    except Exception as error:
        print("\nOcurrio un error inesperado.")
        print(f"Detalle: {error}")


if __name__ == "__main__":
    main()
