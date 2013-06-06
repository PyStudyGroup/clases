#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 6 Unidad 7 Libro.
# Autor:    Alejandro Druetta
# Fecha:    29/05/13
# Versión:  Python 2.7.4

def main():

    fecha = (31, "Dic", 1999)
    diaSiguienteT(fecha)

def diaSiguienteT(fecha):
    diasMeses = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    meses = ("Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Set", "Oct", "Nov", "Dic")
    dia, mes, anio = fecha

    for i in range(len(meses)):
        if meses[i] == mes:
            numeroMes = i

    if dia > diasMeses[numeroMes]:
        print "Error: El mes %s tiene %d días." % (mes, diasMeses[numeroMes])
    elif dia == diasMeses[numeroMes]:
        dia = 1
        if numeroMes == 11:
            numeroMes = 0
            anio += 1
        else:
            numeroMes += 1
    else:
        dia += 1

    print fecha
    print dia, meses[numeroMes], anio

main()
