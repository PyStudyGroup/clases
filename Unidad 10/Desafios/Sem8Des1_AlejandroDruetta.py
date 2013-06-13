#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Autor: Alejandro Druetta
# Fecha: 10/06/13

""" El programa determina si la cadena ingresada es un número flotante
    válido. """

import os

def validar_caracteres(numero):
    """ Verifica que la cadena ingresada esté formada exclusivamente 
        por los caracteres de la cadena car_validos. """

    car_validos = "+-.1234567890eE"

    for i in numero:
        if i in car_validos:
            valido = True
        else:
            valido = False
            break

    return valido

def fragmentar(numero):
    """ Fragmenta la cadena para obtener el coeficiente y el exponente
        del número flotante. Busca la 'E' que indica la base y toma el
        segmento anterior y el posterior a la 'E'. Luego, llama a las
        funciones validar_coeficiente y validar_exponente y retorna
        los valores booleanos que obtiene de ellas. """

    for i in range(len(numero)):
        if numero[i] == "E" or numero[i] == "e":
            coeficiente = numero[:i]
            exponente = numero[i+1:]
            break
        else:
            coeficiente = numero
            exponente = "1"

    print("\nCoeficiente: '%s', Base: 10 y Exponente: '%s'"
          % (coeficiente, exponente))

    coeficiente = validar_coeficiente(coeficiente)
    exponente = validar_exponente(exponente)

    return coeficiente, exponente

def validar_coeficiente(coeficiente):
    """ Verifica que el coeficiente no sea vacío, que no tenga más de
        un '.', un '+' y un '-', y que, en caso de existir, la 
        posición de '+' o '-' ocupe la primera posición. """

    if coeficiente == "" \
        or coeficiente.count("+") > 1 \
        or coeficiente.count("-") > 1 \
        or coeficiente.count(".") > 1 \
        or "+" in coeficiente[1:] \
        or "-" in coeficiente[1:]:
        return False
    else:
        return True

def validar_exponente(exponente):
    """ Verifica que el exponente no tenga una o más 'E' ni '.', que 
        '+' y '-' no se repitan y que, en caso de existir, ocupen la 
        primera posición. """

    if "e" in exponente \
        or exponente.count("+") > 1 \
        or exponente.count("-") > 1 \
        or "." in exponente \
        or "+" in exponente[1:] \
        or "-" in exponente[1:]:
        return False
    else:
        return True

def main():

    coeficiente = False
    exponente = False
    
    while True:

        os.system('clear')

        numero = input("Ingrese un número flotante ('S' para salir): ")

        if numero.lower() == "s":
            break
        else:
            # Verifica que los caracteres que forman el número sean 
            # los permitidos en car_validos.
            if validar_caracteres(numero):
                # Fragmenta el número para obtener el coeficiente y el
                # exponente, y verifica que estén bien formados. 
                coeficiente, exponente = fragmentar(numero)

        if coeficiente and exponente:
            input("\n¡Es un número flotante!")
        else:
            numero = input("\nError: ¡No es un número flotante!")

main()
