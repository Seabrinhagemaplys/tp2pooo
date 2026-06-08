from enum import Enum
from collections.abc import Callable


class EnumCor(Enum):
    BRANCO = "Branco"
    PRETO = "Preto"

class EnumCaracteres(Enum):
    PEAO_BRANCO = "♙"
    PEAO_PRETO = "♟"
    CAVALO_BRANCO = "♘"
    CAVALO_PRETO = "♞"
    BISPO_BRANCO = "♗"
    BISPO_PRETO = "♝"
    TORRE_BRANCO = "♖"
    TORRE_PRETO = "♜"
    RAINHA_BRANCO = "♕"
    RAINHA_PRETO = "♛"
    REI_BRANCO = "♔"
    REI_PRETO = "♚"


def validar_string(string: str) -> bool:
    """
    Valida se uma string está vazia e se o objeto passado é uma instância de string
    """
    if not string.strip():
        return False
    if not isinstance(string, str):
        return False
    
    return True

def checar_instancia_int(numero: int) -> bool:
    """
    Checa se um objeto é um inteiro e retorna booleano associado ao resultado
    """
    if not isinstance(numero, int):
        return False
    
    return True
    