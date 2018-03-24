# -----------------------------------------------------------------------------

import os
from pprint import pprint
from util.timeit import timeit
from modelo.manejo_muestras import *

# -----------------------------------------------------------------------------

# Constantes para archivos

RUTA_ACTAS = os.path.join("archivos", "actas.csv")
RUTA_INDICADORES = os.path.join("archivos", "indicadores.csv")

# -----------------------------------------------------------------------------


@timeit
def generar_muestra_pais(n):
    return generar_muestra_pais_aux(n, RUTA_ACTAS, RUTA_INDICADORES)

# -----------------------------------------------------------------------------


@timeit
def generar_muestra_provincia(n, nombre_provincia):
    return generar_muestra_provincia_aux(n, nombre_provincia,
                                         RUTA_ACTAS, RUTA_INDICADORES)

# -----------------------------------------------------------------------------


if __name__ == "__main__":
    muestra = generar_muestra_pais(8)
    print("Tamaño de la muestra: " + str(len(muestra)))
    pprint(muestra)


# -----------------------------------------------------------------------------
