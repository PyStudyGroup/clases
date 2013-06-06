#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 4 Unidad 7 Libro.
# Autor:    Alejandro Druetta
# Fecha:    28/05/13
# Versión:  Python 2.7.4

def main():

    tiempos = ((10, 41, 23), (8, 50, 12))
    segundos = asegundos(tiempos)
    a_hsmisg(segundos)

def asegundos(tiempos):
    segundos = 0
    for i in range(2):
        hs, mi, sg = tiempos[i]
        segundos += hs * 3600 + mi * 60 + sg
    return segundos

def a_hsmisg(segundos):
    hs = segundos // 3600
    mi = (segundos % 3600) // 60
    sg = (segundos % 3600) % 60
    print hs, "horas,", mi, "minutos y", sg, "segundos."

main()
