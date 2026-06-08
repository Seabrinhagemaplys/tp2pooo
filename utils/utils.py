def validar_string(string: str) -> bool:
    """
    Valida se uma string está vazia e se o objeto passado é uma instância de string
    """
    if not string.strip():
        return False
    if not isinstance(string, str):
        return False
    
    return True