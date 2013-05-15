#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Unidad 4 - Libro 4.3

def main():
    
    linea = "*" * 79
    
    x1 = float(raw_input("X1: "))
    y1 = float(raw_input("Y1: "))
    h1 = pitagoras(x1, y1)
    print ""
    x2 = float(raw_input("X2: "))
    y2 = float(raw_input("Y2: "))
    h2 = pitagoras(x2, y2)
    print ""
    x3 = float(raw_input("X3: "))
    y3 = float(raw_input("Y3: "))
    h3 = pitagoras(x3, y3)
    print ""
    
    print linea
        
    h_max = mayor(h1, h2, h3)
    
    if h_max == h1:
        print "El punto (" + str(x1) + "," + str(y1) + ") está más lejos del centro de coordenadas."
    elif h_max == h2:
        print "El punto (" + str(x2) + "," + str(y2) + ") está más lejos del centro de coordenadas."
    else:
        print "El punto (" + str(x3) + "," + str(y3) + ") está más lejos del centro de coordenadas."
    
    print linea

def pitagoras(x, y):
    
    h = (x**2 + y**2) ** 0.5
    return h

def mayor(h1, h2, h3):
    
    if h3 <= h1 >= h2:
        return h1
    elif h3 <= h2 >= h1:
        return h2
    else:
        return h3
    
main()
