
import pandas


path = 'indicadores cantonales.csv'


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
