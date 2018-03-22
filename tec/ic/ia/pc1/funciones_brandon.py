
from funciones_julian import *
from funciones_armando import *

from sys import exit
from pandas import read_csv
from random import randint, seed
from numpy.random import choice

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




def obtener_datos_de_junta(junta, datos):

    """
    Wrapper para obtener una junta, pues no existe la junta 5402
    :param junta: un numero de junta existente
    :param datos: lista de listas con los datos
    :return: la lista con los datos de la junta correspondiente
    """

    if junta == 5402: return []
    return obtener_fila_por_elemento1(junta, datos)




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

        porcentaje1 = round(numero_x_cada_100 / (numero_x_cada_100 + 100) * 100, 2)

        return porcentaje1, 100 - porcentaje1

    except Exception as error:
        print('convertir_relacion_a_porcentaje: ' + str(error))
        exit(-1)




def random_con_porcentajes(lista_atributos):

    """
    Espera una lista de atributos y su porcentaje en tuplas y genera un aleatorio
    :param lista_atributos: candidatos a escogerse
                            tiene la forma: [('tipo1', %), ('tipo2', %)]
    :return: uno de los tipos de los candidatos, i.e 'tipo1'
    """

    try:
        numero_random = randint(0, 9999)
        porcent_acumulado = lista_atributos[0][1]*100

        for tipo, porcent in lista_atributos:
            if numero_random < porcent_acumulado:
                return tipo, numero_random
            porcent_acumulado += porcent*100

    except Exception as error:
        print('random_general: ' + str(error))
        exit(-1)

def random_con_porcentajes_numpy(lista_atributos, lista_porcentajes):

    """
    Espera una lista de atributos y su porcentaje en tuplas y genera un aleatorio
    :param lista_atributos: lista de atributos posibles
    :param lista_porcentajes: lista de porcentajes para cada atributo
    :return: uno de los tipos de los candidatos, i.e 'tipo1'
    """

    try:
        return choice(lista_atributos, p=lista_porcentajes)

    except Exception as error:
        print('random_general: ' + str(error))
        exit(-1)

"""
l = []
for i in range(1,100000):
    l.append(random_con_porcentajes_numpy(['tipo1','tipo2','tipo3'], [0.1,0.3,0.6]))
    
"""

l = []
for i in range(1,100000):
    l.append(random_con_porcentajes([('1',10),('2',30),('3',60)]))

