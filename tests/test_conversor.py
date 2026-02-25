from services.conversor import binario_para_decimal_e_hex


def test_binario_para_decimal_e_hex_1010():
    decimal, hexadecimal = binario_para_decimal_e_hex("1010")
    assert decimal == 10
    assert hexadecimal == "A"


def test_binario_para_decimal_e_hex_11111111():
    decimal, hexadecimal = binario_para_decimal_e_hex("11111111")
    assert decimal == 255
    assert hexadecimal == "FF"