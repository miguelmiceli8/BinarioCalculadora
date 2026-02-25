def binario_valido(valor: str) -> bool:
    """
    Retorna True se a string for um binário válido (apenas 0 e 1).
    """
    if not isinstance(valor, str) or not valor:
        return False

    return all(c in "01" for c in valor)