# -----------------------------------------------------------------------------


class Fuente:
    CYAN = '\033[96m'
    AZUL = '\033[94m'
    VERDE = '\033[92m'
    MORADO = '\033[93m'
    ROJO = '\033[91m'
    NEGRITA = '\033[1m'
    SUBRAYADO = '\033[4m'
    FIN = '\033[0m'

# -----------------------------------------------------------------------------


def print_error(descripcion_error):
    print(Fuente.ROJO + descripcion_error + Fuente.FIN)

# -----------------------------------------------------------------------------
