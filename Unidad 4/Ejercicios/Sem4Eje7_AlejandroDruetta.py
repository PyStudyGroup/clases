#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Unidad 4 - Ejercicio 7

# Escriba un programa que pida los coeficientes de una ecuación de primer 
# grado (a x + b = 0) y escriba la solución.

def main():
    
    print "Ecuación a x + b = 0"
    a = float(raw_input("Escriba el valor del coeficiente a: "))
    b = float(raw_input("Escriba el valor del coeficiente b: "))
    
    if a == 0 and b != 0:
        print "La ecuación no tiene solución."
    elif a == 0 == b:
        print "Todos los números son solución."
    else:    
        x = -b / a
        print "La solución es:", x
    
main()
