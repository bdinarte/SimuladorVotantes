# -----------------------------------------------------------------------------

import os
import pytest
from g03 import *

"""
Módulo para probar cuanto dura tomar un muestra de 10^n elementos. 
Es un prueba de larga duración (2mins en promedio) y utiliza el máximo del cpu.
"""

# -----------------------------------------------------------------------------


def test_generar_muestra_pais():

    print("\nResultados de país")

    ruta_actas = os.path.join("..", "archivos", "actas.csv")
    ruta_indicadores = os.path.join("..", "archivos", "indicadores.csv")

    # Decorador para tomar el tiempo de la función
    @timeit
    def tiempo_generar_muestra_pais(x):
        return generar_muestra_pais_aux(x, ruta_actas, ruta_indicadores)

    # Empieza con 10 muestras y termina con 100k
    for n in range(1, 6):
        tiempo_generar_muestra_pais(10**n)

# -----------------------------------------------------------------------------


def test_generar_muestra_provincia():

    ruta_actas = os.path.join("..", "archivos", "actas.csv")
    ruta_indicadores = os.path.join("..", "archivos", "indicadores.csv")

    # Decorador para tomar el tiempo de la función
    @timeit
    def tiempo_generar_muestra_provincia(x, prov):

        return generar_muestra_provincia_aux(
            x, prov, ruta_actas, ruta_indicadores
        )

    provincias = [
        "CARTAGO", "ALAJUELA", "HEREDIA", "PUNTARENAS",
        "GUANACASTE", "LIMON", "SAN JOSE"
    ]

    # Empieza con 10 muestras y termina con 100k, esto para cada una de
    # las provincias

    for provincia in provincias:

        print("Provincia: " + provincia)

        for n in range(1, 6):
            tiempo_generar_muestra_provincia(10 ** n, provincia)

# -----------------------------------------------------------------------------
