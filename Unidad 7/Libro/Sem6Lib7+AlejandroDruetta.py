#!/usr/bin/env python
# coding: latin1

# Ejercicio 7 Unidad 7 Libro.
# Autor:    Alejandro Druetta
# Fecha:    27/05/13
# Versión:  Python 2.7.4

def main():
    """ Módulo para inscribir alumnos al curso """

    print "Inscripcion en el curso."
    padron=input("Ingresa un padrón (<=0 para terminar): ")

    ins = []
    while padron > 0:
        if padron not in ins:
            ins.append(padron)
        else:
            print "Ya figura en la lista"
        padron=input("Ingresá un padrón (<=0 para terminar): ")

    print "Esta es la lista de inscriptos: ", ins

    """ Módulo para borrar alumnos de la lista """

    print "Borrar inscripcion en el curso."
    padron=input("Ingresa un padrón (<=0 para terminar): ")

    while padron > 0:
        if padron in ins:
            ins.remove(padron)
        else:
            print "No figura en la lista"
        padron=input("Ingresá un padrón (<=0 para terminar): ")

    print "Esta es la lista de inscriptos: ", ins

main()
