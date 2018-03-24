# -----------------------------------------------------------------------------

from sys import exit
from random import randint
from modelo.manejo_consultas import *

# -----------------------------------------------------------------------------


def convertir_relacion_a_porcentaje(num_x_cada_100):

    """
    Toma una relacion como N elementos por cada 100 elementos de tipo2
    y la convierte a dos porcentajes equivalentes.
    :param num_x_cada_100: cantidad de elementos del tipo 1
    :return: una tupla ordenada con los porcentajes para cada tipo
    """

    try:

        if num_x_cada_100 <= 0:
            raise Exception('Entrada invalida.')

        porcentaje1 = round(num_x_cada_100 / (num_x_cada_100 + 100) * 100, 2)

        return porcentaje1, 100 - porcentaje1

    except Exception as error:
        print('convertir_relacion_a_porcentaje: ' + str(error))
        exit(-1)

# -----------------------------------------------------------------------------


def random_cero_cien(valor_comparacion):
    """
    Funcion encargada de generar un random de cero a 100 para saber si un
    indicador es positivo o negativo para un determinado individuo
    :param valor_comparacion: es el porcentaje que posee el indicador
    para saber si es positivo o negativo
    :return: valor booleano, que indica si el numero generado se encuentra
    en el rango del valor de comparacion o no.
    """
    numero_random = randint(0, 100)
    if numero_random <= int(valor_comparacion):
        return True

    return False

# -----------------------------------------------------------------------------


def random_sexo(razon_masculinidad):
    """
    Funcion encargada de generar un random para saber si un individuo
    es hombre o mujer
    :param razon_masculinidad: es el indice de hombres por cada 100 mujeres
    :return: valor de string indicando el sexo
    """

    porc_hombre = int(razon_masculinidad/(razon_masculinidad+100)*100)
    if random_cero_cien(porc_hombre):
        return 'M'

    return 'F'

# -----------------------------------------------------------------------------


def random_indicadores(datos_indicadores, canton):
    """
    Funcion encargada de obtener los indicadores de un cierto canton, tomar
    los campos a los que se les debe aplicar un random y llamar a las
    respectivas funciones. Al final debe crear una lista con todos los
    indicadores que devuelvan dichas funciones secundarias.
    :param datos_indicadores: es el conjunto de todos los indicadores, leidos
    del archivo indicadores.csv
    :param canton: es sobre el cual se tomaran los indicadores
    :return: una lista con los K atributos/indicadores que tendra el individuo
    """

    indicadores = obtener_datos_canton(datos_indicadores, canton)

    return indicadores

# -----------------------------------------------------------------------------