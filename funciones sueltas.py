
import pandas


path = 'indicadores cantonales.csv'
actas_ordenadas = 'ActasOrdenadas.csv'


def csv_a_listas(ruta_csv):

    """
    Requiere de biblioteca "pandas"
    """
    
    dataframe = pandas.read_csv(ruta_csv)
    return dataframe.values.tolist()



def obtener_indicadores_canton(canton, indicadores):

    """
    Requiere acceso a la lista de listas de momento
    """
    
    fila = [x for x in indicadores if x[1] == canton]
    return fila[0]



def convertir_relacion_a_porcentaje(numero_x_cada_100):

    """
    Entradas
    - numero_x_cada_100: cantidad X por cada 100 elementos del otro tipo
    Salidas
    - porcentaje del tipo 1, porcentaje del tipo 2 (tupla)
    """
    
    porcentaje1 = numero_x_cada_100/(numero_x_cada_100 + 100)

    return porcentaje1, 1 - porcentaje1

