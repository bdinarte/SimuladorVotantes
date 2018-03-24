# -----------------------------------------------------------------------------

import pandas as pd
from g01 import *
from funciones_brandon import generar_buckets
from fuentes import Fuente
from string import ascii_uppercase as ascii
from multiprocessing import Pool, TimeoutError, Condition
from multiprocessing import Process, Lock

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


def obtener_dataframe(ruta_csv, ordenar=False, encabezado=False):

    """
    Lee un dataframe desde un csv. Como el encabezado no nos sirve, se ignora
    @param ruta_csv: nombre completo del archivo csv
    @param ordenar: Se debe o no ordenar las filas por la primera columna
    @param encabezado: Boolean que dice si dejar o no el encabezado leído
    en el csv
    @return: Dataframe donde la columna 0 son los nombres de los cantones, la
    columna corresponde a la provincia de ese canton.
    """

    try:

        if encabezado:
            dataframe = pd.read_csv(ruta_csv)

        else:

            # Si no se indica encabezado se crea uno por defecto
            dataframe = pd.read_csv(ruta_csv, skiprows=[0], header=None)
            dataframe.columns = crear_encabezado(len(dataframe.columns))

        # Ordena las filas por la primera columna
        if ordenar:
            dataframe = dataframe.sort_values(by="A")

        # Se coloca cual columna se utiliza para busquedas
        return dataframe.set_index(dataframe.columns[0])

    except FileNotFoundError or TypeError:
        print(Fuente.ROJO + "Archivo no encontrado: " + ruta_csv + Fuente.FIN)
        exit(-1)

# -----------------------------------------------------------------------------


def obtener_datos_canton(df, canton):

    """
    A partir de un dataframe obtiene la fila que contiene la fila con
    con indicadores para el cantón especificado.
    @param df: Dataframe resultado de leer indicadores.csv
    @param canton: Nombre del cantón del que se necesitan sus indicadores
    @return: lista relacionada con el cantón
    """

    try:
        fila_canton = df.loc[canton]
        return [canton] + fila_canton.values.tolist()
    except KeyError:
        print(Fuente.ROJO + "Cantón no encontrado: " + canton + Fuente.FIN)
        exit(-1)

# -----------------------------------------------------------------------------


def obtener_datos_junta(df, n_junta):

    """
    Obtener una fila según el número de junta
    @param df: Dataframe resultado de leer actas.csv
    @param n_junta: numero de junta
    @return: lista relacionada con la junta
    """

    try:
        if n_junta != 5402:
            return [n_junta] + df.loc[n_junta].values.tolist()
        else:
            return []

    except KeyError:
        print(Fuente.ROJO + "Junta no encontrada: " + str(n_junta) + Fuente.FIN)
        exit(-1)

# -----------------------------------------------------------------------------


def obtener_datos_juntas_random(df, n_juntas):

    """
    Obtiene varias filas de forma aleatoria
    @param df: Dataframe resultado de leer actas.csv
    @param n_juntas: numero de filas que se extraeran
    @return: Dataframe con n cantidad de juntas escogidas aleatoriamente
    TODO: Solo es para probar la eficiencia en test_eficiencia.py
    """

    return df.sample(n=n_juntas, replace=True)

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
        return df.loc[df.PROVINCIA == provincia]
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

    df_total_votos = df["VOTOS RECIBIDOS"]
    df_total_votos = df_total_votos.values.tolist()
    return df_total_votos

# -----------------------------------------------------------------------------


def obtener_juntas(df):

    """
    A partir del dataframe de actas extrae todos los numeros de junta
    @param df: Dataframe resultado de leer actas.csv
    @return: Lista de python con los números de juntas
    """

    # La 'primary key' o index contiene los numeros de juntas
    return df.index.get_values()

# -----------------------------------------------------------------------------


def obtener_opciones_voto(df):

    """
    A partir del dataframe de actas extrae todos los partidos
    @param df: Dataframe resultado de leer actas.csv
    @return: Lista de python con los partidos
    """

    partidos = df.columns.values.tolist()

    # Los primeros dos corresponden a la columna Provincia y Canton.
    return partidos[2:len(partidos) - 1]

# -----------------------------------------------------------------------------


def generar_muestra_threads(n_muestras, df_juntas):

    """
    Generar un conjunto de "votantes" mediante la función
    generar_muestra(n,_muestras, df_juntas) pero usando 4 procesos
    simultaneos, al final se unen los resultados obtenidos de cada uno.
    @param n_muestras: Cantidad de "votantes" que se deben generar
    @param df_juntas: Dataframe que contiene la información de las juntas
    @return: Lista con sublistas, donde cada sublista es un votante
    """

    # Cantidad de procesos que generarán muestras
    n_procesos = 8

    # Variables compartidas por los diferentes procesos
    df_indicadores = funcJ.obtener_dataframe(ruta_indicadores, ordenar=True)
    partidos = funcJ.obtener_opciones_voto(df_juntas)
    lista_juntas = funcJ.obtener_juntas(df_juntas)
    total_votos = funcJ.obtener_total_votos(df_juntas)
    juntas_con_pesos = generar_buckets(lista_juntas, total_votos)

    # Si cada proceso tuviese que hacer menos de 25 muestras (podría ser
    # cualquier otro número mayor a 4), resulta mejor usar solo un proceso
    if n_muestras < n_procesos * 25:
        return generar_muestra(n_muestras, df_juntas, df_indicadores, partidos,
                               juntas_con_pesos)

    pool = Pool(processes=n_procesos)

    # 1 parte de las muestras serán generadas por cada proceso
    muestras_x_proceso = n_muestras // n_procesos

    # Se especifica que función debe correr cada proceso
    # Los primeros tres corren la misma cantidad
    procesos = [
        pool.apply_async(generar_muestra,
                         (muestras_x_proceso, df_juntas, df_indicadores,
                          partidos, juntas_con_pesos,))
        for _ in range(n_procesos-1)
    ]

    # El último genera la cantidad que le corresponde más lo que hace falta
    muestras_restantes = n_muestras - (muestras_x_proceso * n_procesos)

    procesos.append(
        pool.apply_async(generar_muestra,
                         (muestras_x_proceso + muestras_restantes,
                          df_juntas,  df_indicadores, partidos,
                          juntas_con_pesos,))
    )

    # La función sum une las listas de listas obtenidas de cada proceso
    return sum([res.get() for res in procesos], [])

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

    # Indicadores de solo los cantones de Alajuela
    df_provincia = df.loc[df.B == "ALAJUELA"]
    print(Fuente.MORADO + "Indicadores de solo Alajuela" + Fuente.FIN)
    print(df_provincia)

# -----------------------------------------------------------------------------


def test_consultas_actas():

    # df es la abreviación de Dataframe
    # Obtener la tabla de indices cantonales
    df = obtener_dataframe(ruta_actas, encabezado=True)
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
    lista_votos = obtener_total_votos(df)
    print(Fuente.MORADO + "Total de votos" + Fuente.FIN)
    print(lista_votos)

    # Obtiene una lista con los nombres de todos los partidos
    lista_partidos = obtener_opciones_voto(df)
    print(Fuente.MORADO + "Lista de partidos" + Fuente.FIN)
    print(lista_partidos)

    # Obtiene una lista de todas los números de junta
    lista_juntas = obtener_juntas(df)
    print(Fuente.MORADO + "Lista de juntas" + Fuente.FIN)
    print(lista_juntas)

# -----------------------------------------------------------------------------


if __name__ == "__main__":

    test_consultas_actas()
    test_consultas_indicadores()

# -----------------------------------------------------------------------------

