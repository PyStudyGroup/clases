#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Unidad 4 - Ejercicio 6

# Escriba un programa que pida un año y que escriba si es bisiesto o no. 
# Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos
# de 100 no lo son, aunque los múltiplos de 400 sí.

def main():
    
        print "Comprobador de años bisiestos"
        year = int(raw_input("Escriba un año y le diré si es bisiesto: "))
        
        mult_4 = year % 4
        mult_4 = not mult_4
        mult_100 = year % 100
        mult_100 = not mult_100
        mult_400 = year % 400
        mult_400 = not mult_400
                
        if mult_4 and not mult_100:
            print "Sí, el año", year, "es un año bisiesto porque es múltiplo de 4."
        elif mult_400 and mult_100:
            print "Sí, el año", year, "es un año bisiesto porque es múltiplo de 400."
        else:
            print "No, el año", year, "no es un año bisiesto."
          
main()
