# ----------------------------------------------------------------------------------------------------------------------

import time
import random
import numpy as np
from fuentes import Fuente
from pprint import pprint
from funciones_armando import *
from funciones_brandon import *

# ----------------------------------------------------------------------------------------------------------------------


def generar_muestra_pais(canton, indicadores):

    # probando las funciones de brandon
    fila = [x for x in indicadores if x[1] == canton]
    return fila[0]

# ----------------------------------------------------------------------------------------------------------------------


# def obtener_cantidad_cantones_x_provincia(desde, hasta):
#     fila = [x for x in datos if x[1] == canton]
#     return fila[0]

# ----------------------------------------------------------------------------------------------------------------------


def generar_aleatorio_rango(desde, hasta):
    return random.randint(desde, hasta)

# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":

    print(Fuente.MORADO + "Indicadores cantonales" + Fuente.FIN)
    datos = np.array(csv_a_listas(indicadores_cantonales))
    pprint(datos)

    print(Fuente.MORADO + "Indicadores de Cartago como provincia" + Fuente.FIN)
    pprint(obtener_indicadores_provincia("CARTAGO", datos))

    print(Fuente.MORADO + "Indicadores de San Jose como canton" + Fuente.FIN)
    pprint(obtener_indicadores_canton("SAN JOSE", datos))

    # Si se piden 100 votantes
    # Se toma la cantidad de población de cada provincia
    # Usando la función obtener_indicadores_provincia file 2 (desde 0)

    # Se toma cuantos habitantes de cada provincia se deben generar
    # Puede ser un diccionario
    # habitantes_a_generar_por_provincia = {
    #   "CARTAGO": 10
    #   "SAN JOSE": 20
    #   "ALAJUELA: 15
    #   ...
    # }

# ----------------------------------------------------------------------------------------------------------------------
