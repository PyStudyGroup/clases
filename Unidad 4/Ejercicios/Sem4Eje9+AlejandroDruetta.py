#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Unidad 4 - Ejercicio 9

# Escriba un programa que pregunte primero si se quiere calcular el área
# de un triángulo o la de un círculo. Si se contesta que se quiere 
# calcular el área de un triángulo, el programa tiene que pedir entonces
# la base y la altura y escribir el área. Si se contesta que se quiere 
# calcular el área de un círculo, el programa tiene que pedir 
# entonces el radio y escribir el área.

def main():
    
    print """Cálculo de áreas - Elija una figura geométrica:
a) Triángulo.
b) Círculo."""
    figura = raw_input("¿Qué figura quiere calcular?: ")
    
    if figura == "a":
        base = float(raw_input("Escriba la base: "))
        altura = float(raw_input("Escriba la altura: "))
        area = (base * altura) / 2
        print "Un triángulo de base", base, "y altura", altura, "tiene un área de", area
        
    elif figura == "b":
        radio = float(raw_input("Escriba el radio: "))
        pi = 3.141592
        area = (pi * radio) ** 2
        print "Un círculo de radio", radio, "tiene un área de", area
        
    else:
        print "Error: Opción inexistente!"
    
main()
