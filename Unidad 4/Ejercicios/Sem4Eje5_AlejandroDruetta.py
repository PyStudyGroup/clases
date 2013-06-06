#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Unidad 4 - Ejercicio 5

# Escriba un programa que pida tres números y que escriba si son los tres 
# iguales, si hay dos iguales o si son los tres distintos.

def main():
    
    print "Comparador de números"
    n1 = float(raw_input("Escriba un número: "))
    n2 = float(raw_input("Escriba otro número: "))
    n3 = float(raw_input("Escriba otro número: "))
    
    linea = "*" * 50
    
    print linea
    if n1 == n2 == n3:
        print "Ha escrito tres veces el mismo número."
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print "Ha escrito dos veces un mismo número."
    else:
        print "Los tres números que ha escrito son distintos."
    print linea
    
main()
