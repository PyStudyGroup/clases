#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Semana 6 - Libro Unidad 6
# Autor:    Alejandro Druetta
# Fecha:    26/05/13
# Python:   2.7.4

def main():

    while True:

        print "*" * 80
        print """Ejercicios del Libro (Unidad 6) \n
    1. Ejercicio 6.1. Muestra los caracteres de una cadena del ﬁnal al 
                      principio.
    2. Ejercicio 6.4. Cuenta cuántas veces aparece un carácter l dado en
                      una cadena x.
    3. Ejercicio 6.5. ¿Hay más letras “A” o más letras “E” en una cadena?
    4. Ejercicio 6.6. Cuenta cúantas veces aparecen cada una de las
                      vocales en una cadena. No importa si la vocal
                      aparece en mayúscula o en minúscula. \n"""
        print "*" * 80,

        opcion = raw_input("\nIngrese una opción ('S' para salir): ")

        if opcion.lower() == "s":
            break

        elif opcion in "1234":
            print
            cadena = raw_input("Escriba algo: ")

            if opcion == "1":
                ejercicio61(cadena)
            elif opcion == "2":
                ejercicio64(cadena)
            elif opcion == "3":
                ejercicio65(cadena)
            elif opcion == "4":
                ejercicio66(cadena)

        else:
            print "Opción incorrecta."

        print
        raw_input("'Enter' para continuar.")
    
        import os
        os.system('clear')

def ejercicio61(cadena):

    salida = ""

    for i in range(len(cadena)):
        salida += cadena[-i-1]
    print salida

def ejercicio64(cadena):

    def contar(letra, cadena):
        contador = 0
        for i in cadena:
            if i == letra:
                contador += 1
        return contador

    letra = raw_input("Ingrese un caracter: ")
    print "\nEl caracter '%s' aparece %d veces en '%s'." % (letra, contar(letra, cadena), cadena)

def ejercicio65(cadena):

    a = 0
    e = 0

    for i in cadena:
        i = i.lower()
        if i == "a":
            a += 1
        elif i == "e":
            e += 1

    if a > e:
        print "Hay más letras 'a' (%d) en '%s' que letras 'e' (%d)" % (a, cadena, e)
    elif e > a:
        print "Hay más letras 'e' (%d) en '%s' que letras 'a' (%d)" % (e, cadena, a)
    elif a == 0 == e:
        print "No hay letras 'a' ni 'b' en '%s'" % cadena
    else:
        print "Hay la misma cantidad de letras 'a' y 'e' (%d)" % a

def ejercicio66(cadena):

    cadena = cadena.lower()
    vocales = "aeiou"

    for x in vocales:
        contador = 0
        for y in cadena:
            if y == x:
                contador += 1
        print "Hay %d '%s'." % (contador, x)

main()
