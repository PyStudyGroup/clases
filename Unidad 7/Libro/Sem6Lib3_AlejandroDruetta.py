#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 3 Unidad 7 Libro.
# Autor:    Alejandro Druetta
# Fecha:    28/05/13
# Versión:  Python 2.7.4

def main():

    cartas = ("AD", "AD", "AD", "5T", "AD")
    poker(cartas)

def poker(cartas):
    for i in cartas:
        coincidencias = 0
        for ii in cartas:
            if i == ii:
                coincidencias += 1
        if coincidencias >= 4:
            print "Poker!!!"
            break
main()
