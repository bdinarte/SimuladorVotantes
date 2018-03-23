# -----------------------------------------------------------------------------

from time import time
import funciones_julian as funcJ
import funciones_brandon as funcB

# -----------------------------------------------------------------------------

# Variables globales para archivos

ruta_actas = "archivos/actas.csv"
ruta_indicadores = "archivos/indicadores.csv"

# -----------------------------------------------------------------------------

# Funcion solicitada en la especificacion


def generar_muestra_pais(n):

    try:

        global ruta_actas

        juntas_pais = funcJ.obtener_dataframe(ruta_actas, encabezado=True)
        return funcJ.generar_muestra_threads(n, juntas_pais)

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
        return funcJ.generar_muestra_threads(n, juntas_prov)

    except Exception as error:
        print("generar_muestra_pais: " + str(error))
        exit(-1)

# -----------------------------------------------------------------------------

# Funcion compartida


def generar_muestra(n, df_juntas):

    try:
        global ruta_indicadores

        muestra = []

        df_indicadores = funcJ.obtener_dataframe(ruta_indicadores, ordenar=True)

        partidos = funcJ.obtener_opciones_voto(df_juntas)
        lista_juntas = funcJ.obtener_juntas(df_juntas)
        total_votos = funcJ.obtener_total_votos(df_juntas)

        for num_muestra in range(0, n):

            junta_random = funcB.random_con_pesos(lista_juntas, total_votos)
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
    resultado = generar_muestra_provincia(100000, 'ALAJUELA')
    print(resultado)
    print(len(resultado))
    print(time() - start_time)