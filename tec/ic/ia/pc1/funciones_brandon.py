import pandas

from funciones_julian import *
from funciones_armando import *

indicadores_cantonales = 'archivos/indicadores_cantonales.csv'
actas_ordenadas = 'archivos/actas_ordenadas.csv'


def csv_a_listas(ruta_csv):

    """
    Requiere de biblioteca <pandas>
    :param ruta_csv: Ruta del archivo .csv
    :return: Lista con un elemento por cada fila del objeto de <pandas>
    """
    
    dataframe = pandas.read_csv(ruta_csv)
    return dataframe.values.tolist()


def obtener_indicadores_canton(canton, datos):

    """
    Requiere acceso a una lista de listas con los indicadores.
    :param canton: nombre del canton, i.e 'SANTA ANA' 'BUENOS AIRES' 'ASERRI'
    :param datos: Lista de listas con los indicadores cantonales, un canton o provincia por elemento
    :return: Lista con los indicadores del canton especificado
    """
    
    fila = [x for x in datos if x[1] == canton]
    return fila[0]


def obtener_indicadores_provincia(provincia, datos):

    """
    Requiere acceso a una lista de listas con los indicadores.
    :param provincia: nombre de la provincia, i.e 'SAN JOSE' 'CARTAGO'
    :param datos: Lista de listas con los indicadores cantonales, un canton o provincia por elemento
    :return: Lista con los indicadores de la provincia
    """

    fila = [x for x in datos if x[0] == provincia and x[1] == 'PROVINCIA']
    return fila[0]


def convertir_relacion_a_porcentaje(numero_x_cada_100):

    """
    Toma una relacion como N elementos por cada 100 elementos de tipo2
    y la convierte a dos porcentajes equivalentes.
    :param numero_x_cada_100: cantidad de elementos del tipo 1
    :return: una tupla ordenada con los porcentajes para cada tipo
    """

    porcentaje1 = numero_x_cada_100/(numero_x_cada_100 + 100)

    return porcentaje1, 1 - porcentaje1

