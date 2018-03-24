# -----------------------------------------------------------------------------

import os
from time import time
import funciones_julian as funcJ
import funciones_brandon as funcB

# -----------------------------------------------------------------------------

# Variables globales para archivos

ruta_actas = os.path.join("archivos", "actas.csv")
ruta_indicadores = os.path.join("archivos", "indicadores.csv")

# -----------------------------------------------------------------------------

# Funcion solicitada en la especificacion


def generar_muestra_pais(n):

    try:

        global ruta_actas

        juntas_pais = funcJ.obtener_dataframe(ruta_actas, encabezado=True)
        return funcJ.generar_muestra_multiproceso(n, juntas_pais)

    except Exception as error:
        print("generar_muestra_pais: " + str(error))
        exit(-1)

# -----------------------------------------------------------------------------

# Funcion solicitada en la especificacion


def generar_muestra_provincia(n, nombre_provincia):

    try:
        global ruta_actas

        juntas_pais = funcJ.obtener_dataframe(ruta_actas, encabezado=True)
        juntas_prov = funcJ.obtener_datos_juntas_provincia(juntas_pais,
                                                           nombre_provincia
                                                           )
        return funcJ.generar_muestra_multiproceso(n, juntas_prov)

    except Exception as error:
        print("generar_muestra_pais: " + str(error))
        exit(-1)

# -----------------------------------------------------------------------------

# Funcion compartida


def generar_muestra(n, df_juntas, df_indicadores, partidos, juntas_con_pesos):

    try:
        global ruta_indicadores

        muestra = []

        for num_muestra in range(0, n):

            junta_random = funcB.random_de_juntas(juntas_con_pesos)
            datos_junta = funcJ.obtener_datos_junta(df_juntas, junta_random)
            votos_junta = datos_junta[3:18]
            voto_muestra = funcB.random_con_pesos(partidos, votos_junta)

            canton = datos_junta[2]
            indicador_muestra = funcB.random_indicadores(df_indicadores,
                                                         canton
                                                         )
            indicador_muestra.append(voto_muestra)
            muestra.append(indicador_muestra)

        return muestra

    except Exception as error:
        print("generar_muestra: " + str(error))
        exit(-1)

"""
import csv

def writecsv(lista):

    with open("output.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(lista)

"""

if __name__ == "__main__":
    start_time = time()
    resultado = generar_muestra_pais(100000)
<<<<<<< HEAD
=======
    print(resultado)
>>>>>>> 4cdbe450822bc80722489ae976b1148ebd946f1a
    print(len(resultado))
    print(time() - start_time)