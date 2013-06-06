#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 8 Unidad 7 Libro.
# Autor:    Alejandro Druetta
# Fecha:    29/05/13
# Versión:  Python 2.7.4

def main():
    """ Módulo para inscribir alumnos al curso """

    print "Inscripcion en el curso."
    ins = []

    while True:
        existe = False
        nroPadron=input("Ingresa un padrón (<=0 para terminar): ")
        for i in ins:
            if nroPadron in i:
                existe = True
                break
        if nroPadron == 0:
            break
        elif not existe:
            nombre=raw_input("Ingresa el nombre: ")
            apellido=raw_input("Ingresa el apellido: ")
            padron=(nroPadron, nombre, apellido)
            ins.append(padron)
        else:
            print "Ya figura en la lista"

    print "Esta es la lista de inscriptos: ", ins

    """ Módulo para borrar alumnos de la lista """

    print "Borrar inscripción en el curso."
    nroPadron=input("Ingresa un padrón (<=0 para terminar): ")

    while nroPadron > 0:
        for i in ins:
            if nroPadron in i:
                ins.remove(i)
            else:
                print "No figura en la lista"
        nroPadron=input("Ingresá un padrón (<=0 para terminar): ")

    print "Esta es la lista de inscriptos: ", ins

main()
