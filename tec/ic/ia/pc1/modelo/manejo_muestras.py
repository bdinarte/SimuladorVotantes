# -----------------------------------------------------------------------------

from modelo.gen_randoms import *
from modelo.manejo_archivos import *
from modelo.manejo_consultas import *
from multiprocessing import Pool, cpu_count

# -----------------------------------------------------------------------------


def generar_muestra_pais_aux(n, ruta_actas, ruta_indicadores):

    """
    TODO: Documentar
    @param n:
    @param ruta_actas:
    @param ruta_indicadores:
    @return:
    """

    juntas_pais = obtener_dataframe(ruta_actas, encabezado=True)
    df_indicadores = obtener_dataframe(ruta_indicadores, ordenar=True)
    return generar_muestra_threads(n, juntas_pais, df_indicadores)

# -----------------------------------------------------------------------------


def generar_muestra_provincia_aux(n, provincia, ruta_actas, ruta_indicadores):

    """
    TODO: Documentar
    @param n:
    @param provincia:
    @param ruta_actas:
    @param ruta_indicadores:
    @return:
    """

    juntas_pais = obtener_dataframe(ruta_actas, encabezado=True)
    juntas_prov = obtener_datos_juntas_provincia(juntas_pais, provincia)
    df_indicadores = obtener_dataframe(ruta_indicadores, ordenar=True)
    return generar_muestra_threads(n, juntas_prov, df_indicadores)

# -----------------------------------------------------------------------------


def generar_muestra_threads(n_muestras, df_juntas, df_indicadores):

    """
    Generar un conjunto de "votantes" mediante la función
    generar_muestra(n,_muestras, df_juntas) pero usando 4 procesos
    simultaneos, al final se unen los resultados obtenidos de cada uno.
    @param n_muestras: Cantidad de "votantes" que se deben generar
    @param df_juntas: Dataframe que contiene la información de las juntas
    @param df_indicadores: Dataframe con los indicadores de cada cantón
    @return: Lista con sublistas, donde cada sublista es un votante
    """

    # Se genera un proceso por cada núcleo del procesador
    # Se resta 1 para que el porcentaje de uso del procesador no llegue al 100%
    n_procesos = cpu_count() - 1

    # Variables compartidas por los diferentes procesos
    partidos = obtener_opciones_voto(df_juntas)
    lista_juntas = obtener_juntas(df_juntas)
    total_votos = obtener_total_votos(df_juntas)
    juntas_con_pesos = generar_buckets(lista_juntas, total_votos)

    # Si cada proceso tuviese que hacer menos de 25 muestras (podría ser
    # cualquier otro número mayor a 4), resulta mejor usar solo un proceso
    if n_muestras < n_procesos * 25:
        return generar_muestra(n_muestras, df_juntas, df_indicadores, partidos,
                               juntas_con_pesos)

    pool = Pool(processes=n_procesos)

    # 1 parte de las muestras serán generadas por cada proceso
    muestras_x_proceso = n_muestras // n_procesos

    # Se especifica que función debe correr cada proceso
    # Los primeros tres corren la misma cantidad
    procesos = [
        pool.apply_async(generar_muestra,
                         (muestras_x_proceso, df_juntas, df_indicadores,
                          partidos, juntas_con_pesos,))
        for _ in range(n_procesos-1)
    ]

    # El último genera la cantidad que le corresponde más lo que hace falta
    muestras_restantes = n_muestras - (muestras_x_proceso * n_procesos)

    procesos.append(
        pool.apply_async(generar_muestra,
                         (muestras_x_proceso + muestras_restantes,
                          df_juntas,  df_indicadores, partidos,
                          juntas_con_pesos,))
    )

    # La función sum une las listas de listas obtenidas de cada proceso
    return sum([res.get() for res in procesos], [])

# -----------------------------------------------------------------------------


def generar_muestra(n, df_juntas, df_indicadores, partidos, juntas_con_pesos):

    muestra = []

    for num_muestra in range(0, n):

        junta_random = random_de_juntas(juntas_con_pesos)
        datos_junta = obtener_datos_junta(df_juntas, junta_random)
        votos_junta = datos_junta[3:18]
        voto_muestra = random_con_pesos(partidos, votos_junta)

        canton = datos_junta[2]
        indic_muestra = random_indicadores(df_indicadores, canton)
        indic_muestra.append(voto_muestra)
        muestra.append(indic_muestra)

    return muestra

# -----------------------------------------------------------------------------
