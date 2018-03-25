# -----------------------------------------------------------------------------

import os
import pytest
import pandas as pd

from g03 import *
from modelo.manejo_archivos import *

"""
Módulo para generar muestras y escribirlas en un csv para luego realizar el
análisis correspondiente. 
"""

# -----------------------------------------------------------------------------

encabezado = [
    "CANTON", "EDAD", "ES URBANO", "SEXO", "ES DEPENDIENTE",
    "ESTADO VIVIENDA", "E.HACINAMIENTO", "ALFABETIZACIÓN",
    "ESCOLARIDAD PROMEDIO", "ASISTENCIA EDUCACION", "FUERZA DE TRABAJO",
    "SEGURO", "N.EXTRANJERO", "C.DISCAPACIDAD", "POBLACION TOTAL",
    "SUPERFICIE", "DENSIDAD POBLACION", "VIVIENDAS INDIVIDUALES OCUPADAS",
    "PROMEDIO DE OCUPANTES", "P.JEFAT.FEMENINA", "P.JEFAT.COMPARTIDA"
]

# -----------------------------------------------------------------------------


def ejecutar_analisis_muestra_pais(lista_muestra, ruta_salida):

    # Se crear un Dataframe para poder nombrar las columnas y sea fácil de
    # visualizar
    df_muestra = pd.DataFrame(lista_muestra, columns=encabezado)

    # Guardar el archivo y mostrarlo al finalizar
    guardar_como_csv(df_muestra, ruta_salida)

    # Se trata de abrir el archivo generado, sino, no hay problema
    try:
        os.startfile(ruta_salida)
    except PermissionError:
        print("No se pudo abrir el archivo generado")


# -----------------------------------------------------------------------------


if __name__ == "__main__":

    ruta_actas = os.path.join("..", "archivos", "actas.csv")
    ruta_indicadores = os.path.join("..", "archivos", "indicadores.csv")
    ruta_votantes = os.path.join("..", "archivos", "votantes.csv")

    # Con 100 votantes se considera suficiente para ser revisado manualmente
    # e incluso notar una distribución en los datos
    muestra = generar_muestra_pais_aux(100, ruta_actas, ruta_indicadores)

    # Se crea y abre el csv generado
    ejecutar_analisis_muestra_pais(muestra, ruta_votantes)

# -----------------------------------------------------------------------------
