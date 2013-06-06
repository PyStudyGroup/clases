#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Unidad 4 - Ejercicio 1

# Escriba un programa que pida dos números enteros y que calcule su 
# división, escribiendo si la división es exacta o no.

def main():
    
    print "Divisor de números"
    dividendo = int(raw_input("Escriba el dividendo: "))
    divisor = int(raw_input("Escriba el divisor: "))
    
    if divisor == 0:
        print "No se puede dividir por 0."
    else:
        cociente = dividendo // divisor
        resto = dividendo % divisor
        if resto == 0:
            print "La división es exacta. Cociente:", cociente
        else:
            print "La división no es exacta. Cociente:", cociente, "Resto:", resto
    
main()
