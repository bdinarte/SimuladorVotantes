# -----------------------------------------------------------------------------

import random
import numpy as np
from time import time

import pandas as pd
from fuentes import Fuente
from string import ascii_uppercase as ascii

# -----------------------------------------------------------------------------

# Configurar pandas para solo mostrar una tablaña
pd.set_option("display.max_columns", 7)
pd.set_option("display.max_rows", 10)

# -----------------------------------------------------------------------------

# Variables para obtener los csv
ruta_actas_ordenadas = 'archivos/actas.csv'
ruta_indicadores_cantonales = 'archivos/indicadores.csv'

# -----------------------------------------------------------------------------


def crear_encabezado(n_columnas):

    """
    Función para generar los encabezados de un dataframe al igual que
    los de excel, es decir, ['A', 'B', 'C', 'D' ... 'AA', 'AB', 'AC' ... }
    @param n_columnas: cantidad de columnas que contiene el dataframe
    @return: lista de nombres de columnas para un dataframe
    """

    if n_columnas <= 26:
        return list(ascii[0:n_columnas])
    else:
        combinaciones = [l1 + l2 for l1 in ascii for l2 in ascii]
        return list(ascii) + combinaciones[0:n_columnas - 26]

# -----------------------------------------------------------------------------


def obtener_dataframe(ruta_csv):

    """
    Lee un dataframe desde un csv. Como el encabezado no nos sirve, se ignora
    @param ruta_csv: nombre completo del archivo csv
    @param columnas: lista con el nombre de cada columna
    @param index: cual de las columnas se utiliza para realizar busquedas
    @return: Dataframe donde la columna 0 son los nombres de los cantones, la
    columna corresponde a la provincia de ese canton.
    """

    try:

        # El nombre de las columnas es muy largo, por tanto, se remplazan
        # con letras
        dataframe = pd.read_csv(ruta_csv, skiprows=[0],
                                header=None, names=columnas)

        # Se coloca cual columna se utiliza para busquedas
        return dataframe.set_index("A")

    except FileNotFoundError:
        print(Fuente.ROJO + "obtener_dataframe()" + Fuente.FIN)

# -----------------------------------------------------------------------------


def ordenar_datos_x_columna(datos, columna_n):

    """
    Utilizada para ordenar los datos y hacer las extracciones de datos
    de forma más eficiente.
    @param datos: Dataframe resultado de leer un archivo csv
    @param columna_n: Columna por la que se quiere ordenar
    @return: Dataframe que se recibió de entrada pero con las filas en orden
    """

    return datos.sort_values(by=columna_n)

# -----------------------------------------------------------------------------


def obtener_datos_canton(datos, canton):

    """
    A partir de un dataframe obtiene la fila que contiene los indicadores
    para el canton especificado.
    @param datos: Dataframe resultado de leer un archivo csv
    @param canton: Nombre del canton del que se necesitan sus indicadores
    @return: Dataframe de una fila que contiene los indicadores
    """

    # La columna 0 es donde se encuentra el cantón
    filas = datos["A"].isin([canton])

    # Tomar todas las filas donde la columna 0 sea el cantón
    return datos[filas]


# -----------------------------------------------------------------------------

def obtener_datos_juntas_provincia(datos, provincia):

    """
    A partir de un dataframe obtiene los indicadores de todos los cantones
    que pertenecen a una provincia.
    @param datos: Dataframe resultado de leer un archivo csv
    @param provincia: Nombre de la provincia de la que se necesitan los
    indicadores de todos sus cantones
    @return: Dataframe que contiene los indicadores de todos los cantones de
    una provincia
    """

    # La columna 1 es donde se encuentra la provincia
    filas = datos["B"].isin([provincia])

    # Tomar todas las filas donde la columna 1 sea la provincia
    return datos[filas]

# -----------------------------------------------------------------------------

def obtener_datos_junta(datos, junta):

    """
    Obti
    @param datos: Dataframe resultado de leer un archivo csv
    @param junta: numero de junta
    @return: pd.Series (fila) relacionada con la junta
    """
    return datos.loc[junta]

# -----------------------------------------------------------------------------


def test_indicadores():

    # df es la abreviación de Dataframe
    # Obtener la tabla de indices cantonales
    df = obtener_dataframe(ruta_indicadores_cantonales,
                           columnas_indicadores_cantonales, "A")

    print(Fuente.MORADO + "Indicadores cantonales" + Fuente.FIN)
    print(df)

    # Toma los datos de un canton
    datos_canton = obtener_datos_canton(df, "GRECIA")
    print(Fuente.MORADO + "Indicadores cantonales de Grecia" + Fuente.FIN)
    print(datos_canton)
    #
    # # Toma solo los datos de los cantones de una provincia
    # datos_cantones_provincia = obtener_datos_cantones_provincia(df, "ALAJUELA")
    # print(Fuente.MORADO + "Indicadores de cantones de Alajuela" + Fuente.FIN)
    # print(datos_cantones_provincia)
    #
    # # Datos de solo las provincias
    # datos_provincias = obtener_datos_provincias(df)
    # print(Fuente.MORADO + "Indicadores de provincias" + Fuente.FIN)
    # print(datos_provincias)
    #
    # # Indicadores de solo la provincia de Alajuela
    # datos_provincia = obtener_datos_provincia(df, "ALAJUELA")
    # print(Fuente.MORADO + "Indicadores de solo Alajuela" + Fuente.FIN)
    # print(datos_provincia)

# -----------------------------------------------------------------------------


# if __name__ == "__main__":
#     # test_indicadores()
#     df = pd.read_csv(ruta_actas_ordenadas, skiprows=[0], header=None,
#     names=list("ABCDEFGHIJKLMNOPQR"))
#     df.set_index("A", inplace=True)
#     print(df)
#     datos_juntas = obtener_datos_junta(df, 5000)
#     print(datos_juntas.to_frame().T["B"])
#
#     from funciones_brandon import *
#     df = csv_a_listas(ruta_actas_ordenadas)
#     datos_juntas = obtener_datos_de_junta(5000, df)
#     print(datos_juntas)
#
#     actas_ordenadas = ruta_actas_ordenadas
#     datos = csv_a_listas(actas_ordenadas)
#
#     start_time = time()
#
#     for i in range(0, 100000):
#         obtener_datos_de_junta(randint(1,5000), datos)
#
#     print(time() - start_time)
#     print('\n')
#
#     actas_ordenadas = ruta_actas_ordenadas
#     datos = pd.read_csv(ruta_actas_ordenadas, skiprows=[0], header=None, names=list('ABCDEFGHIJKLMNOPQR'))
#     datos.set_index("A", inplace=True)
#
#     start_time = time()
#     for i in range(0, 100000):
#         obtener_datos_junta(datos, randint(1, 5000))
#
#     print(time() - start_time)
#     print('\n')

# -----------------------------------------------------------------------------

