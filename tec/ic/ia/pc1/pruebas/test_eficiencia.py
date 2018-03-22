
#------------------------------------------------------------------------------

import pytest

from funciones_julian import *
from funciones_armando import *
from funciones_brandon import *
from time import time

#------------------------------------------------------------------------------

def test_obtener_fila_por_elemento1():

    actas_ordenadas = '../archivos/actas.csv'
    datos = csv_a_listas(actas_ordenadas)

    start_time = time()

    resultados = []
    for i in range(0,100000):
        resultados.append(obtener_datos_de_junta(randint(1,5000),datos))

    print( time() - start_time )
    print('\n')
    assert len(resultados) == 100000
    # print(l[:100])

#------------------------------------------------------------------------------