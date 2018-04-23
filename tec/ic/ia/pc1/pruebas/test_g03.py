# -----------------------------------------------------------------------------

from g03 import *
from random import seed
from time import time

# -----------------------------------------------------------------------------

"""
Módulo para probar los resultados de las funciones principales del proyecto.
La duración de la prueba es corta, se utilizan muestras pequeñas.
"""

# -----------------------------------------------------------------------------


def test_generar_muestra_pais():

    ruta_a = os.path.join("..", RUTA_ACTAS)
    ruta_a2 = os.path.join("..", RUTA_ACTAS_R2)
    ruta_i = os.path.join("..", RUTA_INDICADORES)

    # Definir una semilla de random fija para obtener resultados consistentes
    seed(2018)

    # Se usa la función auxiliar para reemplazar la ruta de los archivos
    # de prueba
    muestra = generar_muestra_pais_aux(2, ruta_a, ruta_a2, ruta_i)

    assert muestra == [['ACOSTA', 37, 'NO URBANO', 'F', 'NO DEPENDIENTE',
                        'V. MAL ESTADO', 'V. NO HACINADA', 'ALFABETIZADO',
                        6.7, 'EN EDUCACION REGULAR', 'EMPLEADO',
                        'ASEGURADO', 'NO EXTRANJERO', 'NO DISCAPACITADO',
                        20209, 342.2, 59, 5871, 3.44, 26.5, 4.9,
                        'ACCION CIUDADANA', 'ACCION CIUDADANA'],
                       ['SAN JOSE', 23, 'URBANO', 'M', 'NO DEPENDIENTE',
                        'V. BUEN ESTADO', 'V. NO HACINADA', 'ALFABETIZADO',
                        12.3, 'EDUCACION REGULAR INACTIVA', 'DESEMPLEADO',
                        'NO ASEGURADO', 'NO EXTRANJERO', 'NO DISCAPACITADO',
                        288054, 44.6, 6456, 81903, 3.5, 39.6, 6.9,
                        'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL']]

    # Aleatorizar la semilla en caso que la prueba se corra individualmente
    seed(time())

# -----------------------------------------------------------------------------


def test_generar_muestra_provincia():

    ruta_a = os.path.join("..", RUTA_ACTAS)
    ruta_a2 = os.path.join("..", RUTA_ACTAS_R2)
    ruta_i = os.path.join("..", RUTA_INDICADORES)

    # Definir una semilla de random fija para obtener resultados consistentes
    seed(2503)

    # Se usa la función auxiliar para reemplazar la ruta de los archivos
    # de prueba
    muestra = generar_muestra_provincia_aux(2, 'CARTAGO', ruta_a, ruta_a2,
                                            ruta_i)

    assert muestra == [['LA UNION', 31, 'URBANO', 'F', 'NO DEPENDIENTE',
                        'V. BUEN ESTADO', 'V. NO HACINADA', 'ALFABETIZADO',
                        10.2, 'EDUCACION REGULAR INACTIVA', 'EMPLEADO',
                        'ASEGURADO', 'NO EXTRANJERO', 'NO DISCAPACITADO',
                        99399, 44.8, 2217, 26979, 3.67, 31.5, 8.4,
                        'UNIDAD SOCIAL CRISTIANA', 'RESTAURACION NACIONAL'],
                       ['CARTAGO', 51, 'NO URBANO', 'M', 'NO DEPENDIENTE',
                        'V. BUEN ESTADO', 'V. NO HACINADA', 'ALFABETIZADO',
                        6.6, 'EDUCACION REGULAR INACTIVA', 'EMPLEADO',
                        'NO ASEGURADO', 'NO EXTRANJERO', 'NO DISCAPACITADO',
                        147898, 287.8, 514, 38618, 3.8, 28.7, 6.4,
                        'RESTAURACION NACIONAL', 'ACCION CIUDADANA']]

    muestra = generar_muestra_provincia_aux(2, 'HEREDIA', ruta_a, ruta_a2,
                                            ruta_i)

    assert muestra == [['HEREDIA', 36, 'URBANO', 'M', 'NO DEPENDIENTE',
                        'V. BUEN ESTADO', 'V. NO HACINADA', 'ALFABETIZADO',
                        12.2, 'EDUCACION REGULAR INACTIVA', 'DESEMPLEADO',
                        'ASEGURADO', 'NO EXTRANJERO', 'DISCAPACITADO',
                        123616,  282.6, 437, 35216, 3.5, 34.9, 9.2,
                        'ACCION CIUDADANA', 'ACCION CIUDADANA'],
                       ['SARAPIQUI', 57, 'URBANO', 'M', 'NO DEPENDIENTE',
                        'V. BUEN ESTADO', 'V. NO HACINADA', 'ALFABETIZADO',
                        4.6, 'EDUCACION REGULAR INACTIVA', 'DESEMPLEADO',
                        'NO ASEGURADO', 'EXTRANJERO', 'NO DISCAPACITADO',
                        57147, 2140.5, 27, 15768, 3.6, 24.0, 5.9,
                        'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL']]

    # Aleatorizar la semilla en caso que la prueba se corra individualmente
    seed(time())
