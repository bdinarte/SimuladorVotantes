# ----------------------------------------------------------------------------------------------------------------------

import random
import pandas as pd
from fuentes import Fuente

# ----------------------------------------------------------------------------------------------------------------------

# Variables para obtener los csv
ruta_actas_ordenadas = 'archivos/actas_ordenadas.csv'
ruta_indicadores_cantonales = 'archivos/indicadores_cantonales.csv'

# ----------------------------------------------------------------------------------------------------------------------

# Configurar pandas para solo mostrar una tablaña
pd.set_option("display.max_columns", 7)
pd.set_option("display.max_rows", 10)

# ----------------------------------------------------------------------------------------------------------------------


def obtener_dataframe(ruta_csv):
    try:
        return pd.read_csv(ruta_csv, skiprows=[0], header=None)
    except FileNotFoundError:
        print(Fuente.ROJO + "obt_indicadores_cantonales()" + Fuente.FIN)

# ----------------------------------------------------------------------------------------------------------------------


def generar_aleatorio_rango(desde, hasta):
    return random.randint(desde, hasta)

# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":

    # Obtener la tabla de indices cantonales
    datos = obtener_dataframe(ruta_indicadores_cantonales)

    # Ordenar los datos por canton
    datos = datos.sort_values(by=0)
    print(Fuente.MORADO + "Indicadores cantonales" + Fuente.FIN)
    print(datos)

    # Toma los datos de un canton
    datos_canton = datos[datos[0].isin(['GRECIA'])]
    print(Fuente.MORADO + "Indicadores cantonales de Grecia" + Fuente.FIN)
    print(datos_canton)

    # Toma solo los datos de los cantones de una provincia, están ordenados por canton
    datos_cantones_provincia = datos[datos[1].isin(['ALAJUELA'])]
    print(Fuente.MORADO + "Indicadores de cantones de Alajuela" + Fuente.FIN)
    print(datos_cantones_provincia)

    # Datos de solo las provincias
    datos_provincias = datos[datos[0].isin(['PROVINCIA'])]
    print(Fuente.MORADO + "Indicadores de provincias" + Fuente.FIN)
    print(datos_provincias)

    # Indicadores de solo la provincia de Alajuela
    datos_provincia = datos_provincias[datos_provincias[1].isin(['ALAJUELA'])]
    print(Fuente.MORADO + "Indicadores de solo Alajuela" + Fuente.FIN)
    print(datos_provincia)

# ----------------------------------------------------------------------------------------------------------------------
