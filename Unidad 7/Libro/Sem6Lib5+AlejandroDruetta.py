#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 5 Unidad 7 Libro.
# Autor:    Alejandro Druetta
# Fecha:    28/05/13
# Versión:  Python 2.7.4

def main():

    fecha = (31, 12, 1999)
    diaSiguienteE(fecha)



def diaSiguienteE(fecha):
    diasMeses = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    dia = fecha[0]
    mes = fecha[1]
    anio = fecha[2]

    if dia > diasMeses[mes-1]:
        print "Error: El mes %d tiene %d días." % (mes, diasMeses[mes-1])
    elif dia == diasMeses[mes-1]:
        dia = 1
        if mes == 12:
            mes = 1
            anio += 1
        else:
            mes += 1
    else:
        dia += 1

    print fecha
    print dia, mes, anio

main()
