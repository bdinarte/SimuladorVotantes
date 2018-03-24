# -----------------------------------------------------------------------------

from random import randint

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

def random_indicadores(datos_indicadores, canton):

    """
    TODO: Implementar correctamente y documentar
    @param datos_indicadores:
    @param canton:
    @return:
    """

    return [1,'hombre',1,1,1,1,1,1,1]

# -----------------------------------------------------------------------------
