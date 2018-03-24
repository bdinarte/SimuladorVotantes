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
    :return: valor booleano indicando el sexo, el hombre es True
    """

    porc_hombre = razon_masculinidad/(razon_masculinidad+100)*100
    if random_cero_cien(porc_hombre):
        return True

    return False

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


def definir_indicador(funcion, valor, positivo, negativo):
    if funcion(valor):
        return positivo
    return negativo

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
    es_urbano = definir_indicador(
        random_cero_cien, indicadores.J, 'URBANO', 'NO URBANO')

    # --------------- Porcentaje de hombres por cada cien mujeres
    sexo = definir_indicador(random_sexo, indicadores.K, 'M', 'F')

    # --------------- Porcentaje de dependencia demografica
    f = lambda porcentaje: edad >= 65 and random_cero_cien(porcentaje)
    es_dependiente = definir_indicador(
        f, indicadores.L, 'DEPENDIENTE', 'NO DEPENDIENTE')

    # --------------- Porcentaje de viviendas en buen estado
    vivienda_buena = definir_indicador(
        random_cero_cien, indicadores.M, 'V. BUEN ESTADO', 'V. MAL ESTADO')

    # --------------- Porcentaje de viviendas hacinadas
    vivienda_hacinada = definir_indicador(
        random_cero_cien, indicadores.N, 'V. HACINADA', 'V. NO HACINADA')

    # --------------- Porcentaje de Alfabetismo

    alfabetismo = definir_indicador(
        random_cero_cien, indicadores.O if edad <= 24 else indicadores.P,
        'ALFABETIZADO', 'NO ALFABETIZADO')

    # --------------- Porcentaje de escolaridad
    # Se aplica Desviacion estandar de -2 a 2

    escolaridad = indicadores.Q if edad <= 49 else indicadores.R
    escolaridad = round(randint(-2, 2) + escolaridad, 2)

    # --------------- Porcentaje de asistencia a la educacion regular

    educacion_regular = definir_indicador(
        random_cero_cien, indicadores.S if edad <= 24 else indicadores['T'],
        'EN EDUCACION REGULAR', 'EDUCACION REGULAR INACTIVA')

    # --------------- Tasa neta de participacion

    es_empleado = definir_indicador(
        random_cero_cien, indicadores.U if sexo == 'M' else indicadores.V,
        'EMPLEADO', 'DESEMPLEADO')

    # --------------- Porcentaje de ser no asegurado

    es_asegurado = definir_indicador(
        random_cero_cien, indicadores.W if es_empleado == 'EMPLEADO' else indicadores.Z, 'ASEGURADO', 'NO ASEGURADO')

    # --------------- Porcentaje de ser extranjero

    es_extranjero = definir_indicador(
        random_cero_cien, indicadores.X, 'EXTRANJERO', 'NO EXTRANJERO')

    # --------------- Porcentaje de ser discapacitado

    es_discapacitado = definir_indicador(
        random_cero_cien, indicadores.Y, 'DISCAPACITADO', 'NO DISCAPACITADO')

    return indicadores['C':'I'].values.tolist() + [
        canton, edad, es_urbano, sexo, es_dependiente, vivienda_buena,
        vivienda_hacinada, alfabetismo, escolaridad, educacion_regular,
        es_empleado, es_asegurado, es_extranjero, es_discapacitado
    ]

# -----------------------------------------------------------------------------
