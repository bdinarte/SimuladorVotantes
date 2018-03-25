# -----------------------------------------------------------------------------

import os
import pytest
from g03 import *
import pandas as pd

"""
Módulo para generar muestras y escribirlas en un csv para luego realizar el
análisis correspondiente. 
"""

# -----------------------------------------------------------------------------

encabezado = [
    "CANTON", "EDAD", "ES URBANO", "SEXO", "ES DEPENDIENTE",
    "ESTADO VIVIENDA", "E.HACINAMIENTO", "ALFABETIZACIÓN",
    "ESCOLARIDAD PROMEDIO", "ASISTENCIA EDUCACIÓN", "FUERZA DE TRABAJO",
    "SEGURO", "N.EXTRANJERO", "C.DISCAPACIDAD"
]

# -----------------------------------------------------------------------------


def ejecutar_analisis_muestra_pais(lista):

    df = pd.DataFrame(lista, columns=encabezado)

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
