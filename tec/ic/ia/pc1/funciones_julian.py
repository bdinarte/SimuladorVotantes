# -----------------------------------------------------------------------------

import random
import pandas as pd
from fuentes import Fuente

# -----------------------------------------------------------------------------

# Variables para obtener los csv
ruta_actas_ordenadas = 'archivos/actas_ordenadas.csv'
ruta_indicadores_cantonales = 'archivos/indicadores_cantonales.csv'

# -----------------------------------------------------------------------------

# Configurar pandas para solo mostrar una tablaña
pd.set_option("display.max_columns", 7)
pd.set_option("display.max_rows", 10)

# -----------------------------------------------------------------------------


def obtener_dataframe(ruta_csv):

    """
    Lee un dataframe desde un csv. Como el encabezado no nos sirve, se ignora
    @param ruta_csv: nombre completo del archivo csv
    @return: Dataframe donde la columna 0 son los nombres de los cantones, la
    columna corresponde a la provincia de ese canton.
    """

    try:
        return pd.read_csv(ruta_csv, skiprows=[0], header=None)
    except FileNotFoundError:
        print(Fuente.ROJO + "obt_indicadores_cantonales()" + Fuente.FIN)

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
    filas = datos[0].isin([canton])

    # Tomar todas las filas donde la columna 0 sea el cantón
    return datos[filas]


# -----------------------------------------------------------------------------

def obtener_datos_cantones_provincia(datos, provincia):

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
    filas = datos[1].isin([provincia])

    # Tomar todas las filas donde la columna 1 sea la provincia
    return datos[filas]

# -----------------------------------------------------------------------------


def obtener_datos_provincias(datos):

    """
    A partir de un dataframe obtiene los indicadores de todas las provincias,
    no de sus cantones, sino de la provincia en general
    @param datos: Dataframe resultado de leer un archivo csv
    @return: Dataframe que contiene los indicadores de todas las provincias
    """

    # La columna 0 es donde se encuentra el canton, sin embargo, el "canton"
    # provincia, significa que es para la provincia en general, pues así,
    # se acordo por el grupo de trabajo
    filas = datos[0].isin(['PROVINCIA'])
    return datos[filas]


# -----------------------------------------------------------------------------

def obtener_datos_provincia(datos, provincia):

    """
    A partir de un dataframe obtiene los indicadores para solamente
    una provincia
    @param datos: Dataframe resultado de leer un archivo csv
    @param provincia: Nombre de la provincia de la cual se necesitan
    su indicadores
    @return: Dataframe que contiene los indicadores de solo una provincia
    """

    # Se obtienen los datos de solo provincias
    provincias = obtener_datos_provincias(datos)

    # De esas provincias se toma solo la que se necesita
    return provincias[provincias[1].isin([provincia])]


# -----------------------------------------------------------------------------

if __name__ == "__main__":

    # df es la abreviación de Dataframe
    # Obtener la tabla de indices cantonales
    df = obtener_dataframe(ruta_indicadores_cantonales)

    # Ordenar los datos por canton
    df = ordenar_datos_x_columna(df, 0)
    print(Fuente.MORADO + "Indicadores cantonales" + Fuente.FIN)
    print(df)

    # Toma los datos de un canton
    datos_canton = obtener_datos_canton(df, "GRECIA")
    print(Fuente.MORADO + "Indicadores cantonales de Grecia" + Fuente.FIN)
    print(datos_canton)

    # Toma solo los datos de los cantones de una provincia
    datos_cantones_provincia = obtener_datos_cantones_provincia(df, "ALAJUELA")
    print(Fuente.MORADO + "Indicadores de cantones de Alajuela" + Fuente.FIN)
    print(datos_cantones_provincia)

    # Datos de solo las provincias
    datos_provincias = obtener_datos_provincias(df)
    print(Fuente.MORADO + "Indicadores de provincias" + Fuente.FIN)
    print(datos_provincias)

    # Indicadores de solo la provincia de Alajuela
    datos_provincia = obtener_datos_provincia(df, "ALAJUELA")
    print(Fuente.MORADO + "Indicadores de solo Alajuela" + Fuente.FIN)
    print(datos_provincia)

# ----------------------------------------------------------------------------------------------------------------------
