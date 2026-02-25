def binario_para_decimal_e_hex(numero: str) -> tuple[int, str]:
    """
    Converte um número binário (string) para decimal e hexadecimal.
    Retorna uma tupla: (decimal, hexadecimal).
    """
    numero_preenchido = numero
    while len(numero_preenchido) % 4 != 0:
        numero_preenchido = "0" + numero_preenchido

    tabela_hex = {
        "0000": "0", "0001": "1", "0010": "2", "0011": "3",
        "0100": "4", "0101": "5", "0110": "6", "0111": "7",
        "1000": "8", "1001": "9", "1010": "A", "1011": "B",
        "1100": "C", "1101": "D", "1110": "E", "1111": "F"
    }

    hexadecimal = ""
    for i in range(0, len(numero_preenchido), 4):
        grupo = numero_preenchido[i:i + 4]
        hexadecimal += tabela_hex[grupo]

    decimal = int(numero, 2)
    return decimal, hexadecimal