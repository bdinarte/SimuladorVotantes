# -----------------------------------------------------------------------------

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

        juntas_pais = funcJ.obtener_dataframe(ruta_actas)
        return generar_muestra(n, juntas_pais)

    except Exception as error:
        print("generar_muestra_pais: " + str(error))
        exit(-1)

# -----------------------------------------------------------------------------

# Funcion solicitada en la especificacion


def generar_muestra_provincia(n, nombre_provincia):

    try:
        global ruta_actas

        juntas_pais = funcJ.obtener_dataframe(ruta_actas)
        juntas_prov = funcJ.obtener_datos_juntas_provincia(juntas_pais,
                                                           nombre_provincia
                                                           )
        return generar_muestra(n, juntas_prov)

    except Exception as error:
        print("generar_muestra_pais: " + str(error))
        exit(-1)

# -----------------------------------------------------------------------------

# Funcion compartida


def generar_muestra(n, datos_juntas):

    try:
        global ruta_indicadores

        muestra = []

        datos_indicadores = funcJ.obtener_dataframe(ruta_indicadores)
        partidos = funcJ.obtener_partidos(datos_juntas)
        total_juntas = []
        total_votos = ['OBTENER COLUMNA VOTOS']

        for num_muestra in range(0, len(datos_juntas) - 1):

            junta_random = funcB.random_con_pesos(total_juntas, total_votos)
            votos_junta = ['OBTENER VOTOS PARA UUNA JUNTA']
            voto_muestra = funcB.random_con_pesos(partidos, votos_junta)

            canton = funcJ.obtener_datos_junta(datos_juntas, junta_random)[2]
            indicador_muestra = funcB.random_indicadores(datos_indicadores,
                                                         canton
                                                         )
            indicador_muestra.append(voto_muestra)
            muestra.append(indicador_muestra)

    except Exception as error:
        print("generar_muestra: " + str(error))
        exit(-1)






