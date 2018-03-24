# -----------------------------------------------------------------------------

from util.fuentes import *

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
        return df.loc[canton]
        # return [canton] + fila_canton.values.tolist()
    except KeyError:
        print_error("Cantón no encontrado: " + canton)
        exit(-1)

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


def obtener_datos_junta(df, n_junta):

    """
    Obtener una fila según el número de junta
    @param df: Dataframe resultado de leer actas.csv
    @param n_junta: numero de junta
    @return: pd.Secuence con los datos de la junta
    """

    return df.loc[n_junta]

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
        print_error("Provincia no encontrada: " + provincia)
        exit(-1)

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


def obtener_votos_junta(df):

    """
    Consulta los votos obtenidos para la junta especificada
    @param df: Dataframe de la junta a consultar
    @return: 
    """

    return df["ACCESIBILIDAD SIN EXCLUSION":"BLANCO"]

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
