
from funciones_julian import *
from funciones_armando import *

from sys import exit
from pandas import read_csv
from random import randint, seed
from numpy.random import choice

indicadores_cantonales = 'archivos/indicadores.csv'
actas_ordenadas = 'archivos/actas.csv'




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
    :param datos: Lista de listas con los indicadores cantonales, un canton o
                  provincia por elemento
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


def random_con_pesos(atributos, pesos):

    """
    Genera aleatorio segun porcentajes por cada elemento
    :param atributos: lista de elementos candidatos a escogerse
    :param pesos: lista de porcentajes correspondientes a cada elemento
    :return: uno de los elementos candidatos, i.e 'elemento1'
    """

    try:
        numero_random = randint(0, sum(pesos) * 100 - 1)
        porcent_acumulado = 0

        for i in range(0, len(atributos)):
            porcent_acumulado += pesos[i] * 100
            if numero_random < porcent_acumulado:
                return atributos[i]


    except Exception as error:
        print('random_general: ' + str(error))
        exit(-1)


def random_de_juntas(tipos_repetidos):

    try:
        numero_random = randint(0, len(tipos_repetidos) - 1)
        return tipos_repetidos[numero_random]

    except Exception as error:
        print('random_general: ' + str(error))
        exit(-1)


def generar_buckets(tipos, cantidades):

    contador = 0
    acumulador = []
    for cantidad in cantidades:
        acumulador += [tipos[contador]] * cantidad
        contador += 1

<<<<<<< HEAD
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
=======
    return acumulador
>>>>>>> 8225a648df3fa9d1830414e9405781d75037959a


def random_indicadores(datos_indicadores, canton):

    return [1,'hombre',1,1,1,1,1,1,1]