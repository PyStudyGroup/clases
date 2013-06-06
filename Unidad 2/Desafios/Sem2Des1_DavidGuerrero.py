# -*- coding: utf-8 -*-


def binToDec(strbin):
    """Funcion que convierte una cadena
    binaria a decimal"""

    decimal = 0
    strbin = strbin[::-1]
    for i in range(len(strbin)):
        decimal += int(int(strbin[i]) * (2 ** i))
    return decimal

print binToDec(raw_input("Numero binario:"))
