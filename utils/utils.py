from typing import Literal
from enum import Enum

def validar_string(string: str) -> bool:
    """
    Valida se uma string está vazia e se o objeto passado é uma instância de string
    """
    if not string.strip():
        return False
    if not isinstance(string, str):
        return False
    
    return True

class EnumCor(Enum):
    BRANCO = "Branco"
    PRETO = "Preto"

class EnumCaracteres(Enum):
    PEAO_BRANCO = "♙"
    PEAO_PRETO = "♟"
    CAVALO_BRANCO = "♘"
    CAVALO_PRETO = "♞"
    