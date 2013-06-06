#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio1 - Semana 5
# Autor:    Alejandro Druetta
# Fecha: 23/05/13

def main():

    cadena = raw_input("Escriba una frase: ")
    salida = ""
    print
    
    for letra in cadena:
        salida += letra
        print salida

main()
