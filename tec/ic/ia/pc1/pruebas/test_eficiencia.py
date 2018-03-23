
#------------------------------------------------------------------------------

import pytest

from funciones_julian import *
from funciones_armando import *
from funciones_brandon import *
from time import time

# -----------------------------------------------------------------------------


def test_obtener_fila_por_elemento1():

    actas_ordenadas = '../archivos/actas.csv'
    datos = csv_a_listas(actas_ordenadas)

    start_time = time()

    for i in range(0,100000):
        obtener_datos_de_junta(randint(1,6540), datos)

    print(time() - start_time)
    print('\n')
    # assert len(resultados) == 10000
    # print(l[:100])

# -----------------------------------------------------------------------------


def test_panditas():

    actas_ordenadas = '../archivos/actas_ordenadas.csv'
    datos = obtener_dataframe(actas_ordenadas, columnas=columnas_actas_ordenadas, index="A")

    start_time = time()
    for i in range(0, 100000):
        obtener_datos_junta(datos, randint(1,6540))

    print(time() - start_time)
    print('\n')
    # assert len(resultados) == 10000
    # print(l[:100])

# -----------------------------------------------------------------------------
