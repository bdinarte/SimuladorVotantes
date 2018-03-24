
from funciones_julian import *
from funciones_armando import *

from sys import exit
from pandas import read_csv
from random import randint, seed
from numpy.random import choice

from tec.ic.ia.pc1 import funciones_julian
from tec.ic.ia.pc1.fuentes import Fuente

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

<<<<<<< HEAD
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

    return acumulador
=======
# -----------------------------------------------------------------------------

def obtener_indicadores_canton(df, canton):
>>>>>>> 4cdbe450822bc80722489ae976b1148ebd946f1a

    """
    A partir de un dataframe obtiene las filas de todas los indicadores
    que pertenecen a un canton en especifico.
    @param df: Dataframe resultado de leer indicadores.csv
    @param canton: Nombre del canton del que se necesitan los indicadores
    @return: Dataframe que contiene todos los indicadores de ese canton
    """

    try:
        return [canton] + df.loc[canton].values.tolist()
    except KeyError:
        print(Fuente.ROJO + "Canton no encontrado: " + canton + Fuente.FIN)
        exit(-1)



# -----------------------------------------------------------------------------

def random_indicadores(datos_indicadores, canton):
    """
    Funcion encargada de obtener los indicadores de un cierto canton, tomar
    los campos a los que se les debe aplicar un random y llamar a las respectivas
    funciones. Al final debe crear una lista con todos los indicadores que devuelvan
    dichas funciones secundarias.
    :param datos_indicadores: es el conjunto de todos los indicadores, leidos del archivo indicadores.csv
    :param canton: es sobre el cual se tomaran los indicadores
    :return: una lista con los K atributos/indicadores que tendra el individuo
    """

    indicadores = obtener_indicadores_canton(datos_indicadores, canton)

    return indicadores
