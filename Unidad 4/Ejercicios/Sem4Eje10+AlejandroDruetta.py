#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Unidad 4 - Ejercicio 10

# Escriba un programa que pida una distancia en centímetros y que
# escriba esa distancia en kilómetros, metros y centímetros (escribiendo
# solamente las unidades necesarias).

def main():
        
    linea = "*" * 79
    
    print linea
    print "Convertidor de centímetros a kilómetros, metros y centímetros"
    print linea
    distancia = int(raw_input("Escriba una distancia en centímetros: "))
    
    km, mt, cm = convertir(distancia)
    
    print linea
    print distancia, "centímetros son", 
    
    if km != "0" != mt:
        print km + " km,",
    elif km != "0" == mt and cm != "0":
        print km + " km",
    elif km != "0" and mt == "0" == cm:
        print km + " km."
        
    if mt != "0" != cm:
        print mt + " mt",
    elif mt != "0" == cm:
        print mt + " mt."
        
    if cm != "0" and km == "0" == mt:
        print cm + " cm."        
    elif cm != "0" and (km != "0" or mt != "0"):
        print "y " + cm + " cm."
    
    print linea
    
def convertir(distancia):
    kilometros = distancia / 100000
    metros = (distancia % 100000) / 100
    centimetros = ((distancia % 10000000) % 100)
    
    return str(kilometros), str(metros), str(centimetros)
    
main()
