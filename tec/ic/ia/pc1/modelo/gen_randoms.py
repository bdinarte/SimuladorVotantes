# -----------------------------------------------------------------------------

from random import randint
from modelo.manejo_consultas import *

# -----------------------------------------------------------------------------


def random_con_pesos(atributos, pesos):

    """
    Genera aleatorio según porcentajes por cada elemento
    @param atributos: lista de elementos candidatos a escogerse
    @param pesos: lista de porcentajes correspondientes a cada elemento
    @return: uno de los elementos candidatos, i.e 'elemento1'
    """

    numero_random = randint(0, sum(pesos) * 100 - 1)
    porcent_acumulado = 0

    for i in range(0, len(atributos)):
        porcent_acumulado += pesos[i] * 100
        if numero_random < porcent_acumulado:
            return atributos[i]

# -----------------------------------------------------------------------------


def random_de_juntas(tipos_repetidos):

    """
    TODO: Falta documentación
    @param tipos_repetidos:
    @return:
    """

    numero_random = randint(0, len(tipos_repetidos) - 1)
    return tipos_repetidos[numero_random]

# -----------------------------------------------------------------------------


def generar_buckets(tipos, cantidades):

    """
    TODO: Falta documentación
    @param tipos:
    @param cantidades:
    @return:
    """

    contador = 0
    acumulador = []
    for cantidad in cantidades:
        acumulador += [tipos[contador]] * cantidad
        contador += 1

    return acumulador


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

    numero_random = randint(1, 10000)
    if numero_random <= valor_comparacion*100:
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

    porc_hombre = razon_masculinidad/(razon_masculinidad+100)*100
    if random_cero_cien(porc_hombre):
        return 'M'

    return 'F'

# -----------------------------------------------------------------------------


def random_edad():

    """
    Funcion encargada de generar una edad para un individuo
    Segun los datos tomados de los indicadores demograficos
    cantonales del anho 2013. Donde un 69p de personas estan
    entre 18 y 64 anhos, y un 7p de 65 a mas anhos.
    El otro grupo (menores de edad) no se toma en cuenta en la
    edad a generar para los votantes.
    :return: Edad que va ser asignada a un individuo
    """

    numero_random = randint(1, 76)
    if numero_random <= 69:
        return randint(18, 64)

    return randint(64, 100)

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

    # --------------- Generacion de una edad para el individuo
    edad = random_edad()

    # --------------- Porcentaje de la poblacion urbana
    porc_poblacion_urbana = indicadores[1]
    es_urbano = random_cero_cien(porc_poblacion_urbana)

    # --------------- Porcentaje de hombres por cada cien mujeres
    indice_masculinidad = indicadores[1]
    sexo = random_sexo(indice_masculinidad)

    # --------------- Porcentaje de dependencia demografica
    porc_dependencia_demografica = indicadores[1]
    es_dependiente = 'NO DEPENDIENTE'
    if edad >= 65 and random_cero_cien(porc_dependencia_demografica):
        es_dependiente = 'DEPENDIENTE'

    # --------------- Porcentaje de viviendas en buen estado
    porc_viviendas_buenas = indicadores[1]
    vivienda_buena = 'VIVIENDA MALA'
    if random_cero_cien(porc_viviendas_buenas):
        vivienda_buena = 'VIVIENDA BUENA'

    # --------------- Porcentaje de viviendas hacinadas
    porc_viviendas_hacinadas = indicadores[1]
    vivienda_hacinada = 'VIVIENDA NO HACINADA'
    if random_cero_cien(porc_viviendas_hacinadas):
        vivienda_hacinada = 'VIVIENDA HACINADA'

    # --------------- Porcentaje de ser extranjero
    porc_extranjero = indicadores[1]
    es_extranjero = 'NO EXTRANJERO'
    if random_cero_cien(porc_extranjero):
        es_extranjero = 'EXTRANJERO'

    # --------------- Porcentaje de ser discapacitado
    porc_discapacidad = indicadores[1]
    es_discapacitado = 'NO DISCAPACITADO'
    if random_cero_cien(porc_discapacidad):
        es_discapacitado = 'DISCAPACITADO'

    # --------------- Porcentaje de ser no asegurado
    porc_asegurado = indicadores[1]
    es_asegurado = 'NO ASEGURADO'
    if random_cero_cien(porc_asegurado):
        es_asegurado = 'ASEGURADO'

    return indicadores

# -----------------------------------------------------------------------------
