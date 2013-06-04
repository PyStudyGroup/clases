#! /usr/bin/env python
# -*- coding: utf-8 -*-

def a_palabras( frase ):

    permitidos = u"abcdefghijklmnñopqrstuvwxyz áéíóú"
    frase_limp = ""
    frase_min = frase.lower()

    for i in frase_min:
        if i in permitidos:
            frase_limp += i

    palabras = frase_limp.split()

    return palabras

def main():

    diccionario = {}

    lengua = unicode( raw_input( "¿Qué idioma usaremos para la traducción?: " ), "utf-8")

    while True:

        print
        frase = unicode( raw_input( "Escriba una frase completa ('*' para terminar): " ), "utf-8")

        if frase == "*":
            break
        else:
            palabras = a_palabras( frase )

        print

        for i in palabras:

            i = i.title()

            if i not in diccionario:
                significado = unicode( raw_input( "¿Cómo se escribe '%s' en %s?: " % ( i, lengua ) ), "utf-8" )
                significado = significado.lower()
                significado = significado.title()
                diccionario[i] = significado

    print "\nDiccionario: \n"

    for i in diccionario:
        print i, "\t=", diccionario[i]

main()
