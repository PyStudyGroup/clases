#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Unidad 4 - Ejercicio 2

# Escriba un programa que pida dos números y que conteste cuál es el 
# menor y cuál el mayor o que escriba que son iguales.

def main():
    
    num1 = float(raw_input("Escriba un número: "))
    num2 = float(raw_input("Escriba otro número: "))
    
    if num1 == num2:
        print "Los dos números son iguales."
    elif num1 > num2:
        print "Menor:", num2, ";", "Mayor:", num1
    else:
        print "Menor:", num1, ";", "Mayor:", num2

main()
