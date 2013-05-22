#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Semana 5 - Ejercicio 5.3 del Libro
Autor:      Alejandro Druetta
Fecha:      21/05/13
Propósito:  Experimentar los distintos tipos de ciclos.
"""

def main():
    
    # Menú de procedimientos:
             
    print "Procedimientos:\n"
    print "1. Ciclo interactivo."
    print "2. Ciclo con centinela."
    print "3. Ciclo 'inﬁnito' que se rompe.\n"

    opcion = raw_input("Elija un procedimiento (1-3): ")
    print

    while True:
        
        if opcion in "123":
            break
        else:
            opcion = raw_input("Opción incorrecta, intente nuevamente: ")
        
    if opcion == "1":
        ciclo_interactivo()
    elif opcion == "2":
        ciclo_centinela()
    elif opcion == "3":
        ciclo_infinito()

def ciclo_interactivo():
    """Determina si un número es positivo usando un ciclo interactivo."""
    
    opcion = "s"
    while opcion == "s":
        numero = raw_input("Ingrese un número positivo: ")
        controla(numero)
        opcion = raw_input("¿Desea continuar (S/N)?: ")
        opcion = opcion.lower()
    
def ciclo_centinela():
    """Determina si un número es positivo usando un ciclo con centinela."""
    
    numero = ""
    while numero != "*":
        numero = raw_input("Ingrese un número positivo ('*' para salir): ")
        if numero != "*":
            controla(numero)        
    
def ciclo_infinito():
    """Determina si un número es positivo usando un ciclo infinito con break."""
    
    while True:
        numero = raw_input("Ingrese un número positivo ('*' para salir): ")
        if numero != "*":
            controla(numero)
        else:
            break

def controla(numero):
    
    numero = float(numero)
    if numero >= 0:
        print "Correcto!"
    else:
        print "Error: No es un número positivo."    

main()
