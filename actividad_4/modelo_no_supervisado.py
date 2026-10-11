from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


# Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent
DATOS_DIR = BASE_DIR / "datos"
PRUEBAS_DIR = BASE_DIR / "pruebas"

ARCHIVO_DATOS = DATOS_DIR / "dataset_trayectos_no_supervisado.csv"

PRUEBAS_DIR.mkdir(parents=True, exist_ok=True)

# 1. Cargar y validar los datos
df = pd.read_csv(ARCHIVO_DATOS, encoding="utf-8-sig")

columnas_modelo = [
    "numero_estaciones",
    "costo_interno",
    "transbordos",
]

if df.empty:
    raise ValueError("El dataset no contiene registros.")

if df[columnas_modelo].isnull().any().any():
    raise ValueError("Hay valores vacíos en las variables del modelo.")

if len(df) < 3:
    raise ValueError("Se necesitan al menos 3 registros para formar 3 grupos.")

X = df[columnas_modelo]

print("=" * 60)
print("MODELO DE APRENDIZAJE NO SUPERVISADO: K-MEANS")
print("=" * 60)
print(f"Registros cargados: {len(df)}")
print(f"Variables utilizadas: {', '.join(columnas_modelo)}")
print("Tipo de datos: muestra sintética, no registros operativos reales.")

# 2. Normalizar las variables
escalador = StandardScaler()
X_escalado = escalador.fit_transform(X)

# 3. Entrenar K-Means
modelo = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["grupo"] = modelo.fit_predict(X_escalado) + 1

# 4. Evaluar la agrupación
if df["grupo"].nunique() > 1 and df["grupo"].nunique() < len(df):
    silueta = silhouette_score(X_escalado, df["grupo"])
else:
    silueta = None

print("\nCANTIDAD DE TRAYECTOS POR GRUPO")
print(df["grupo"].value_counts().sort_index().to_string())

print("\nCARACTERÍSTICAS PROMEDIO POR GRUPO")
resumen = (
    df.groupby("grupo")[columnas_modelo]
    .mean()
    .round(2)
)
print(resumen.to_string())

if silueta is not None:
    print(f"\nPuntuación de silueta: {silueta:.4f}")
    print("La silueta evalúa la separación y cohesión de los grupos.")
else:
    print("\nNo fue posible calcular la puntuación de silueta.")

# 5. Guardar resultados
archivo_resultados = PRUEBAS_DIR / "resultados_agrupamiento.csv"
df.to_csv(archivo_resultados, index=False, encoding="utf-8-sig")

archivo_resumen = PRUEBAS_DIR / "resumen_grupos.csv"
resumen.to_csv(archivo_resumen, encoding="utf-8-sig")

# 6. Crear una gráfica de los grupos
plt.figure(figsize=(9, 6))

for grupo in sorted(df["grupo"].unique()):
    seleccion = df[df["grupo"] == grupo]
    plt.scatter(
        seleccion["numero_estaciones"],
        seleccion["costo_interno"],
        label=f"Grupo {grupo}",
        s=65
    )

plt.title("Agrupamiento de trayectos de TransMilenio mediante K-Means")
plt.xlabel("Número de estaciones")
plt.ylabel("Costo interno (valor sintético)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

archivo_grafica = PRUEBAS_DIR / "grafica_agrupamiento.png"
plt.savefig(archivo_grafica, dpi=150)
plt.close()

print("\nARCHIVOS GENERADOS")
print(f"- {archivo_resultados}")
print(f"- {archivo_resumen}")
print(f"- {archivo_grafica}")

print("\nIMPORTANTE: los grupos son identificadores del algoritmo.")
print("No representan categorías oficiales de TransMilenio.")
print("Los resultados corresponden únicamente a datos sintéticos.")
