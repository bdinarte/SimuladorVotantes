# -----------------------------------------------------------------------------

import pandas as pd
from fuentes import Fuente
from funciones_brandon import *
from string import ascii_uppercase as ascii

# -----------------------------------------------------------------------------

# Configurar pandas para solo mostrar una tablaña
pd.set_option("display.max_columns", 7)
pd.set_option("display.max_rows", 10)

# -----------------------------------------------------------------------------

# Variables para obtener los csv
ruta_actas = 'archivos/actas.csv'
ruta_indicadores = 'archivos/indicadores.csv'

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


def obtener_dataframe(ruta_csv, ordenar=False):

    """
    Lee un dataframe desde un csv. Como el encabezado no nos sirve, se ignora
    @param ruta_csv: nombre completo del archivo csv
    @param ordenar: Se debe o no ordenar las filas por la primera columna
    @return: Dataframe donde la columna 0 son los nombres de los cantones, la
    columna corresponde a la provincia de ese canton.
    """

    try:

        # El nombre de las columnas es muy largo, por tanto, se remplazan
        # con letras
        dataframe = pd.read_csv(ruta_csv, skiprows=[0], header=None)
        dataframe.columns = crear_encabezado(len(dataframe.columns))

        # Ordena las filas por la primera columna
        if ordenar:
            dataframe = dataframe.sort_values(by="A")

        # Se coloca cual columna se utiliza para busquedas
        return dataframe.set_index("A")

    except FileNotFoundError:
        print(Fuente.ROJO + "Archivo no encontrado: " + ruta_csv + Fuente.FIN)
        exit(-1)

# -----------------------------------------------------------------------------


def obtener_datos_canton(df, canton):

    """
    A partir de un dataframe obtiene la fila que contiene la fila con
    con indicadores para el cantón especificado.
    @param df: Dataframe resultado de leer indicadores.csv
    @param canton: Nombre del cantón del que se necesitan sus indicadores
    @return: pd.Series (fila) relacionada con el cantón
    """

    try:
        return df.loc[canton]
    except KeyError:
        print(Fuente.ROJO + "Cantón no encontrado: " + canton + Fuente.FIN)
        exit(-1)

# -----------------------------------------------------------------------------


def obtener_datos_junta(df, n_junta):

    """
    Obtener una fila según el número de junta
    @param df: Dataframe resultado de leer actas.csv
    @param n_junta: numero de junta
    @return: pd.Series (fila) relacionada con la junta
    """

    try:
        return df.loc[n_junta] if n_junta != 5402 else []
    except KeyError:
        print(Fuente.ROJO + "Junta no encontrada: " + str(n_junta) + Fuente.FIN)
        exit(-1)

# -----------------------------------------------------------------------------


def obtener_datos_juntas_provincia(df, provincia):

    """
    A partir de un dataframe obtiene las filas de todas las juntas
    que pertenecen a una provincia.
    @param df: Dataframe resultado de leer actas.csv
    @param provincia: Nombre de la provincia de la que se necesitan los datos
    de las juntas
    @return: Dataframe que contiene todas las juntas de la provincia
    """

    try:
        return df.loc[df.B == provincia]
    except KeyError:
        print(Fuente.ROJO + "Provincia no encontrada: " + provincia + Fuente.FIN)
        exit(-1)

# -----------------------------------------------------------------------------


def obtener_total_votos(df):

    """
    A partir del dataframe de actas, extrae la columna de votos totales y
    la retorna como una lista
    @param df: Dataframe resultado de leer actas.csv
    @return: Lista de python con los votos totales
    """

    # TODO: Esta debe ser S en vez de R, esta así para que agarre algo
    df_total_votos = df.R
    df_total_votos = df_total_votos.values.tolist()
    return df_total_votos

# -----------------------------------------------------------------------------


def test_consultas_indicadores():

    # df es la abreviación de Dataframe
    # Obtener la tabla de indices cantonales
    df = obtener_dataframe(ruta_indicadores, ordenar=True)
    print(Fuente.MORADO + "Indicadores cantonales" + Fuente.FIN)
    print(df)

    # Toma los datos de un canton
    df_canton = obtener_datos_canton(df, "GRECIA")
    print(Fuente.MORADO + "Indicadores cantonales de Grecia" + Fuente.FIN)
    print(df_canton)

    # Datos de solo las provincias
    df_provincias = df.loc["PROVINCIA"]
    print(Fuente.MORADO + "Indicadores de provincias" + Fuente.FIN)
    print(df_provincias)

    # Indicadores de solo los cantones de Alajuela
    df_provincia = df.loc[df.B == "ALAJUELA"]
    print(Fuente.MORADO + "Indicadores de solo Alajuela" + Fuente.FIN)
    print(df_provincia)

# -----------------------------------------------------------------------------


def test_consultas_actas():

    # df es la abreviación de Dataframe
    # Obtener la tabla de indices cantonales
    df = obtener_dataframe(ruta_actas, ordenar=False)
    print(Fuente.MORADO + "Actas ordenadas" + Fuente.FIN)
    print(df)

    # Obtener una fila según el número de junta.
    df_junta = obtener_datos_junta(df, 4000)
    print(Fuente.MORADO + "Junta 4000" + Fuente.FIN)
    print(df_junta)

    # Obtener todas las juntas que pertencen a una provincia
    df_juntas = obtener_datos_juntas_provincia(df, "ALAJUELA")
    print(Fuente.MORADO + "Juntas de Alajuela" + Fuente.FIN)
    print(df_juntas)

    # Debería ser la columna S pero todavía no está en el csv
    df_total_votos = obtener_total_votos(df)
    print(Fuente.MORADO + "Total de votos" + Fuente.FIN)
    print(df_total_votos)

# -----------------------------------------------------------------------------


if __name__ == "__main__":

    test_consultas_actas()
    test_consultas_indicadores()

# -----------------------------------------------------------------------------

