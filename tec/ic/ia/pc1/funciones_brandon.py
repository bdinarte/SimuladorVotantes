
from funciones_julian import *
from funciones_armando import *

from sys import exit
from pandas import read_csv

indicadores_cantonales = 'archivos/indicadores_cantonales.csv'
actas_ordenadas = 'archivos/actas_ordenadas.csv'



def csv_a_listas(ruta_csv):

    """
    Requiere de biblioteca <pandas>
    :param ruta_csv: Ruta del archivo .csv
    :return: Lista con un elemento por cada fila del objeto de <pandas>
    """

    try:
        dataframe = read_csv(ruta_csv)
        return dataframe.values.tolist()

    except Exception as error:
        print('csv_a_listas: ' + str(error))
        exit(-1)


# Tiene como objetivo obtener una junta o un canton, desde sus respectivos datos

def obtener_fila_por_elemento1(valor_col_1, datos):

    """
    Requiere acceso a una lista de listas con los indicadores.
    :param valor_col_1: valor de la primer columna de los datos
    :param datos: Lista de listas con los datos
    :return: Lista con los elementos que la fila encontrada
    """

    try:
        fila = [x for x in datos if x[0] == valor_col_1]

        if len(fila) == 0:
            raise Exception('No existe el elemento ' + str(valor_col_1) + '.')

        return fila[0]

    except Exception as error:
        print('obtener_fila_por_elemento1: ' + str(error))
        exit(-1)


def obtener_indicadores_provincia(provincia, datos):

    """
    Requiere acceso a una lista de listas con los indicadores.
    :param provincia: nombre de la provincia, i.e 'SAN JOSE' 'CARTAGO'
    :param datos: Lista de listas con los indicadores cantonales, un canton o provincia por elemento
    :return: Lista con los indicadores de la provincia
    """

    try:
        fila = [x for x in datos if x[1] == provincia and x[0] == 'PROVINCIA']

        if len(fila) == 0:
            raise Exception('No existe el elemento ' + str(provincia) + '.')

        return fila[0]

    except Exception as error:
        print('obtener_fila_por_elemento1: ' + str(error))
        exit(-1)



def convertir_relacion_a_porcentaje(numero_x_cada_100):

    """
    Toma una relacion como N elementos por cada 100 elementos de tipo2
    y la convierte a dos porcentajes equivalentes.
    :param numero_x_cada_100: cantidad de elementos del tipo 1
    :return: una tupla ordenada con los porcentajes para cada tipo
    """

    try:

        if numero_x_cada_100 <= 0:
            raise Exception('Entrada invalida.')

        porcentaje1 = numero_x_cada_100 / (numero_x_cada_100 + 100)

        return porcentaje1, 1 - porcentaje1

    except Exception as error:
        print('convertir_relacion_a_porcentaje: ' + str(error))
        exit(-1)