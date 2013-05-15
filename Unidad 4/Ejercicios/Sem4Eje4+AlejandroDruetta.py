#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Unidad 4 - Ejercicio 4

# Escriba un programa que pida dos números enteros y que escriba si el 
# mayor es múltiplo del menor.

def main():
    
    print "Comparador de múltiplos"
    num1 = int(raw_input("Escriba un número: "))
    num2 = int(raw_input("Escriba otro número: "))
    
    mayor, menor = mayor_menor(num1, num2)
    
    if es_multiplo(mayor, menor):
        print mayor, "es múltiplo de", menor
    else:
        print mayor, "no es múltiplo de", menor
    
    
def es_multiplo(mayor, menor):
    if mayor == 0 == menor:
        return True
    elif mayor == 0 or menor == 0:
        return False
    elif mayor % menor == 0:
        return True
    else:
        return False
    
def mayor_menor(num1, num2):
    if num1 > num2:
        return num1, num2
    else:
        return num2, num1

main()
