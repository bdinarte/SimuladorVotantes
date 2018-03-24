# -----------------------------------------------------------------------------

import pandas as pd
from util.fuentes import *
from string import ascii_uppercase as asc

# -----------------------------------------------------------------------------

# Configurar pandas para no imprimir resultados tan grandes
pd.set_option("display.max_columns", 7)
pd.set_option("display.max_rows", 10)

# -----------------------------------------------------------------------------


def obtener_encabezado(n_columnas):
    """
    Función para generar los encabezados de un dataframe al igual que
    los de excel, es decir, ['A', 'B', 'C', 'D' ... 'AA', 'AB', 'AC' ... }
    @param n_columnas: cantidad de columnas que contiene el dataframe
    @return: lista de nombres de columnas para un dataframe
    """

    if n_columnas <= 26:
        return list(asc[0:n_columnas])
    else:
        combinaciones = [l1 + l2 for l1 in asc for l2 in asc]
        return list(asc) + combinaciones[0:n_columnas - 26]

# -----------------------------------------------------------------------------


def leer_csv(ruta_csv, encabezado=False):

    """
    Lee un dataframe desde un csv.
    @param ruta_csv: nombre completo del archivo csv
    @param encabezado: Dice si dejar o no el encabezado leído en el csv
    @return: Dataframe obtenido del csv
    """

    try:
        f = leer_csv_sin_encabezado
        return pd.read_csv(ruta_csv) if encabezado else f(ruta_csv)

    except FileNotFoundError or TypeError:
        print_error("Archivo no encontrado: " + ruta_csv)
        exit(-1)

# -----------------------------------------------------------------------------


def leer_csv_sin_encabezado(ruta_csv):

    """
    Lee un dataframe desde un csv y coloca un encabezado por defecto
    @param ruta_csv: nombre completo del archivo csv
    @return: Dataframe obtenido del csv
    """

    dataframe = pd.read_csv(ruta_csv, skiprows=[0], header=None)
    dataframe.columns = obtener_encabezado(len(dataframe.columns))
    return dataframe

# -----------------------------------------------------------------------------


def obtener_dataframe(ruta_csv, ordenar=False, encabezado=False):

    """
    Lee un dataframe desde un csv.
    @param ruta_csv: nombre completo del archivo csv
    @param ordenar: Se debe o no ordenar las filas por la primera columna
    @param encabezado: Boolean que dice si dejar o no el encabezado leído
    en el csv
    @return: Dataframe donde la columna 0 son los nombres de los cantones, la
    columna corresponde a la provincia de ese canton.
    """

    dataframe = leer_csv(ruta_csv, encabezado)

    # Ordena las filas por la primera columna
    if ordenar:
        dataframe = dataframe.sort_values(by="A")

    # Se coloca cual columna se utiliza para busquedas
    return dataframe.set_index(dataframe.columns[0])

# -----------------------------------------------------------------------------