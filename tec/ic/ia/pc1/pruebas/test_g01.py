# -----------------------------------------------------------------------------

import pytest

from funciones_julian import *
from funciones_armando import *
from funciones_brandon import *

# -----------------------------------------------------------------------------


def test_csv_a_listas():

    """
    Se comprueba que el archivo se abrió correctamente
    """
    listas = csv_a_listas("../archivos/actas_ordenadas.csv")
    assert listas is not None and listas is not []

# -----------------------------------------------------------------------------


def test_obtener_indicadores_canton():

    """
    Se debería obtener únicamente la fila 2 que coincide con Atenas
    No importa la cantidad de atributos, pero si que los obtenga todos
    """

    canton = "ATENAS"
    indicadores = [
        ["GRECIA", "ALAJUELA",76898, 395.7],
        ["ATENAS", "ALAJUELA", 25460, 127.2],
        ["FLORES", "HEREDIA", 20037, 7],
        ["LIBERIA", "GUANACASTE", 62987, 1436.5]
    ]

    fila = obtener_fila_por_elemento1(canton, indicadores)
    assert fila == ["ATENAS", "ALAJUELA", 25460, 127.2]

# -----------------------------------------------------------------------------


def test_obtener_indicadores_provincia():

    """
    Se debería obtener únicamente la fila 3 que coincide con CARTAGO
    No importa la cantidad de atributos, pero si que los obtenga todos
    """

    provincia = "CARTAGO"

    indicadores = [
        ["PROVINCIA", "ALAJUELA", 76898, 395.7],
        ["ATENAS", "ALAJUELA", 25460, 127.2],
        ["PROVINCIA", "CARTAGO", 20037, 7],
        ["LIBERIA", "GUANACASTE", 62987, 1436.5]
    ]

    fila = obtener_indicadores_provincia(provincia, indicadores)
    assert fila == ["PROVINCIA", "CARTAGO", 20037, 7]


# -----------------------------------------------------------------------------

def test_convertir_relacion_a_porcentaje():

    """
    Hay 92 X por cada 100 Y. Por tanto, los porcentajes son 48 y 52
    Además, ambos porcentajes deben sumar 100
    """

    porcentajes = convertir_relacion_a_porcentaje(92)
    assert porcentajes[0] == pytest.approx(48, 0.1)
    assert porcentajes[1] == pytest.approx(52, 0.1)
    assert porcentajes[0] + porcentajes[1] == pytest.approx(100, 0.1)

# -----------------------------------------------------------------------------

def test_obtener_datos_junta():

    """
    Dado un numero de junta, retorna la fila con los votos de la misma
    Debe obtenerse unicamente la segunda fila que corresponde a la 233
    """

    junta = 233
    actas = [
            [1,"ALAJUELA", "ATENAS", 15, 20],
            [233,"SAN JOSE", "ASERRI", 111, 1],
            [99, "HEREDIA", "FLORES", 123, 999]
            ]

    fila = obtener_datos_de_junta(junta, actas)
    assert fila == [233,"SAN JOSE", "ASERRI", 111, 1]

# -----------------------------------------------------------------------------

def test_random_con_porcentajes():

    """
    Se define la semilla del random para obtener datos consistentes
    Se espera que el random genere resultados acorde a los porcentajes
    """

    seed(105)
    resultados = []
    atributos = ['atributo1', 'atributo2', 'atributo3', 'atributo4']
    porcentajes = [5, 5, 80, 10]

    for c in range(0, 10):
        resultados.append(random_con_porcentajes(atributos, porcentajes))

    assert resultados == ['atributo4', 'atributo3', 'atributo4', 'atributo3',
                          'atributo1', 'atributo3', 'atributo3', 'atributo4',
                          'atributo3', 'atributo3'
                          ]