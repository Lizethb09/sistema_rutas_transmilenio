# ============================================
# SISTEMA INTELIGENTE DE BÚSQUEDA DE RUTAS
# TRANSMILENIO - BOGOTÁ
# ============================================

# ============================================
# TARIFA REAL DEL SISTEMA - 2026
# ============================================

TARIFA_TRANSMILENIO = 3550


# ============================================
# BASE DE CONOCIMIENTO
# ============================================

conexiones = {
    "Portal Norte": {
        "Calle 100": 2
    },

    "Calle 100": {
        "Portal Norte": 2,
        "NQS Calle 75": 2
    },

    "NQS Calle 75": {
        "Calle 100": 2,
        "Universidad Nacional": 3,
        "Calle 63": 1
    },

    "Calle 63": {
        "NQS Calle 75": 1,
        "Universidad Nacional": 2
    },

    "Universidad Nacional": {
        "NQS Calle 75": 3,
        "Calle 63": 2,
        "Calle 26": 2
    },

    "Calle 26": {
        "Universidad Nacional": 2,
        "Museo Nacional": 1,
        "San Diego": 2
    },

    "Museo Nacional": {
        "Calle 26": 1,
        "San Diego": 1,
        "Universidades": 2
    },

    "San Diego": {
        "Calle 26": 2,
        "Museo Nacional": 1,
        "Universidades": 1
    },

    "Universidades": {
        "Museo Nacional": 2,
        "San Diego": 1
    }
}


# ============================================
# REGLAS LÓGICAS
# ============================================

def existe_conexion(origen, destino):

    return (
        origen in conexiones
        and destino in conexiones[origen]
    )


def obtener_vecinos(estacion):

    if estacion in conexiones:
        return conexiones[estacion]

    return {}


def obtener_costo(origen, destino):

    if existe_conexion(origen, destino):
        return conexiones[origen][destino]

    return None


# ============================================
# COORDENADAS PARA LA HEURÍSTICA
# ============================================

coordenadas = {
    "Portal Norte": (0, 10),
    "Calle 100": (0, 8),
    "NQS Calle 75": (0, 6),
    "Calle 63": (0, 5),
    "Universidad Nacional": (1, 4),
    "Calle 26": (1, 2),
    "Museo Nacional": (1, 1),
    "San Diego": (2, 1),
    "Universidades": (2, 0)
}


# ============================================
# FUNCIÓN HEURÍSTICA
# ============================================

def heuristica(estacion_actual, destino):

    x1, y1 = coordenadas[estacion_actual]
    x2, y2 = coordenadas[destino]

    return abs(x1 - x2) + abs(y1 - y2)


# ============================================
# ALGORITMO A*
# ============================================

def buscar_ruta_a_estrella(origen, destino):

    if origen not in conexiones:
        return None, "La estación de origen no existe."

    if destino not in conexiones:
        return None, "La estación de destino no existe."

    abiertos = [origen]

    costos = {
        origen: 0
    }

    padres = {
        origen: None
    }

    while abiertos:

        actual = min(
            abiertos,
            key=lambda estacion:
            costos[estacion] +
            heuristica(estacion, destino)
        )

        if actual == destino:

            ruta = []

            while actual is not None:
                ruta.append(actual)
                actual = padres[actual]

            ruta.reverse()

            return ruta, costos[destino]

        abiertos.remove(actual)

        for vecino, costo in obtener_vecinos(actual).items():

            nuevo_costo = costos[actual] + costo

            if (
                vecino not in costos
                or nuevo_costo < costos[vecino]
            ):

                costos[vecino] = nuevo_costo
                padres[vecino] = actual

                if vecino not in abiertos:
                    abiertos.append(vecino)

    return None, "No existe una ruta disponible."


# ============================================
# MOSTRAR ESTACIONES
# ============================================

def mostrar_estaciones():

    print("\nESTACIONES DISPONIBLES")
    print("======================")

    for numero, estacion in enumerate(
        conexiones.keys(),
        start=1
    ):

        print(f"{numero}. {estacion}")


# ============================================
# OBTENER ESTACIÓN POR NÚMERO
# ============================================

def seleccionar_estacion(mensaje):

    estaciones = list(conexiones.keys())

    while True:

        try:

            numero = int(input(mensaje))

            if 1 <= numero <= len(estaciones):

                return estaciones[numero - 1]

            print(
                f"\nError: seleccione un número "
                f"entre 1 y {len(estaciones)}."
            )

        except ValueError:

            print(
                "\nError: debe ingresar un número."
            )


# ============================================
# MOSTRAR RESULTADO
# ============================================

def mostrar_resultado(
    origen,
    destino,
    ruta,
    costo_busqueda
):

    print("\n==============================================")
    print("                 RESULTADO")
    print("==============================================")

    print(f"\nOrigen: {origen}")
    print(f"Destino: {destino}")

    print("\nRuta encontrada:")

    print(" -> ".join(ruta))

    print(f"\nNúmero de estaciones: {len(ruta)}")

    print(
        f"Costo interno de búsqueda A*: "
        f"{costo_busqueda}"
    )

    print(
        f"Tarifa del viaje: "
        f"${TARIFA_TRANSMILENIO:,} COP"
        .replace(",", ".")
    )

    print("\nNota:")

    print(
        "El costo interno es utilizado por el "
        "algoritmo A* para comparar rutas."
    )

    print(
        "No corresponde al precio real cobrado "
        "por cada estación."
    )

    print(
        "La tarifa real corresponde al ingreso "
        "al sistema."
    )


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

print("\n==============================================")
print(" SISTEMA INTELIGENTE DE BÚSQUEDA DE RUTAS")
print("             TRANSMILENIO - BOGOTÁ")
print("==============================================")


# ============================================
# MOSTRAR ESTACIONES
# ============================================

mostrar_estaciones()


# ============================================
# SELECCIONAR ORIGEN
# ============================================

origen = seleccionar_estacion(
    "\nSeleccione el número de la estación de origen: "
)


# ============================================
# SELECCIONAR DESTINO
# ============================================

destino = seleccionar_estacion(
    "Seleccione el número de la estación de destino: "
)


# ============================================
# EVITAR MISMA ESTACIÓN
# ============================================

if origen == destino:

    print("\n==============================================")
    print("RESULTADO")
    print("==============================================")

    print(
        f"\nYa se encuentra en la estación "
        f"{origen}."
    )

    print(
        "No es necesario realizar una búsqueda "
        "de ruta."
    )

else:

    # ========================================
    # EJECUTAR A*
    # ========================================

    print("\nBuscando la mejor ruta...")

    ruta, resultado = buscar_ruta_a_estrella(
        origen,
        destino
    )


    # ========================================
    # MOSTRAR RESULTADO
    # ========================================

    if ruta is not None:

        mostrar_resultado(
            origen,
            destino,
            ruta,
            resultado
        )

    else:

        print("\nError:")
        print(resultado)


# ============================================
# FINAL
# ============================================

print("\n==============================================")
print("Fin del programa")
print("==============================================")