# -----------------------------------------------------------------------------

import pytest

import numpy as np
from funciones_julian import *
from funciones_armando import *
from funciones_brandon import *
from time import time

# -----------------------------------------------------------------------------


def test_obtener_fila_por_elemento1():

    actas = '../archivos/actas.csv'
    datos = csv_a_listas(actas)

    start_time = time()

    for i in range(0,100000):
        obtener_datos_de_junta(randint(1, 6540), datos)

    print(time() - start_time)
    print('\n')

# -----------------------------------------------------------------------------


def test_panditas():

    actas = '../archivos/actas.csv'
    datos = obtener_dataframe(actas, encabezado=True)

    start_time = time()
    datos = obtener_datos_juntas_random(datos, 100000)
    print(datos)

    print(time() - start_time)
    print('\n')

# -----------------------------------------------------------------------------
