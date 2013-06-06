#! /usr/bin/env python
# -*- coding: utf-8 -*-

n = int(raw_input("¿ingrese un Valor ?: "))
suma = 0
for x in range(9):
    print n
    n = n + suma
    suma = suma + 1
    if x == 8:
       salir = raw_input("precione e para salir: ")
       if 'E'== salir:
           break







