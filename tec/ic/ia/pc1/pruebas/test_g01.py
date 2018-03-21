# ----------------------------------------------------------------------------------------------------------------------

import pytest

from funciones_julian import *
from funciones_armando import *
from funciones_brandon import *

# ----------------------------------------------------------------------------------------------------------------------


def test_csv_a_listas():

    """
    Se comprueba que el archivo se abrió correctamente
    """
    listas = csv_a_listas("../archivos/actas_ordenadas.csv")
    assert listas is not None and listas is not []

# ----------------------------------------------------------------------------------------------------------------------


def test_obtener_indicadores_canton():

    """
    Se debería obtener únicamente la fila 2 que coincide con Atenas
    No importa la cantidad de atributos, pero si que los obtenga todos
    """

    canton = "ATENAS"
    indicadores = [
        ["GRECIA", "ALAJUELA", "76 898", "395.7"],
        ["ATENAS", "ALAJUELA", "25 460", "127.2"],
        ["FLORES", "HEREDIA", "20 037", "7"],
        ["LIBERIA", "GUANACASTE", "62 987", "1436.5"]
    ]

    fila = obtener_fila_por_elemento1(canton, indicadores)
    assert fila == ["ATENAS", "ALAJUELA", "25 460", "127.2"]

# ----------------------------------------------------------------------------------------------------------------------


def test_convertir_relacion_a_porcentaje():

    """
    Hay 92 X por cada 100 Y. Por tanto, los porcentajes son 48 y 54 respectivamente
    Además, ambos porcentajes deben sumar 100
    """

    porcentajes = convertir_relacion_a_porcentaje(92)
    assert porcentajes[0] == pytest.approx(0.48, 0.01)
    assert porcentajes[1] == pytest.approx(0.52, 0.01)
    assert porcentajes[0] + porcentajes[1] == 1

# ----------------------------------------------------------------------------------------------------------------------
