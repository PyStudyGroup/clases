#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 9 Unidad 7 Libro.
# Autor:    Alejandro Druetta
# Fecha:    29/05/13
# Versión:  Python 2.7.4

def main():

    cadena = raw_input("Escriba una frase célebre: ")
    puntuacion = "\'\"¡!°@#$%&*-_=+,.;:¿?"
    cadena_limpia = ""
    contador = 0

    for i in cadena:
        if i not in puntuacion:
            cadena_limpia += i

    lista = cadena_limpia.split()

    for i in lista:
        if len(i) > 5:
            contador += 1
            print contador, "-", i.title()

main()
