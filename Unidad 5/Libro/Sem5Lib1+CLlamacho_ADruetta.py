#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Semana 5 - Ejercicio 5.1 del Libro
Autores:    Carlos Llamacho y Alejandro Druetta
Fecha:      20/05/13
"""

def main():
    
    # Menú de procedimientos:
            
    print "Procedimientos:"
    print "1. Ciclo deﬁnido."
    print "2. Ciclo interactivo."
    print "3. Ciclo con centinela."
    print "4. Ciclo 'inﬁnito' que se rompe."
    
    opcion = int(raw_input("Elija un procedimiento (1-4): "))
    
    while True:
                
        if opcion >= 1 and opcion <= 4:     # Alternativa: if opcion in "1234":
            break
        else:
            opcion = int(raw_input("Opción incorrecta, intente nuevamente: "))
main()
