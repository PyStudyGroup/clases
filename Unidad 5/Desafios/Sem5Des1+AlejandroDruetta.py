#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Programa:   Sem5Des1+AlejandroDruetta.py
Autor:      Alejandro Druetta
Fecha:      20/05/13
Versión:    Python 2.7.4

Propósito:  Conversor Binario/Decimal, Decimal/Binario.
"""

def main():
    
    import os    
    os.system('clear')
    
    linea = "-" * 29
    
    while True:
        
        print "Calculadora Binario/Decimal"
        print
        print linea
        print "'b' para convertir a Binario."
        print "'d' para convertir a Decimal."
        print "'s' para salir."
        print linea
        print
        
        opcion = raw_input("Opción: ")
        print
        print linea
        opcion = opcion.lower()
        
        if opcion == "b":
            decimal = raw_input("Digite un decimal: ")
            if comprueba_decimal(decimal):
                decimal = int(decimal)
                print "Resultado: ", a_binario(decimal)
                limpia()
            else:
                print decimal, "no es un decimal."
                limpia()
            
        elif opcion == "d":
            binario = raw_input("Digite un binario: ")
            if comprueba_binario(binario):
                print "Resultado:", a_decimal(binario)
                limpia()
            else:
                print binario, "no es un binario."
                limpia()
            
        elif opcion == "s":
            print "Fin."
            break 
        
        else:
            print "Opción inválida."
            limpia()
    
def comprueba_binario(binario):
    
    bits = "01"
    
    for bit in binario:
        if bit not in bits:
            return False
    return True
            
def comprueba_decimal(decimal):
    
    digitos = "1234567890"
    
    for digito in decimal:
        if digito not in digitos:
            return False
    return True
   
def a_decimal(numero):
    
    expo = len(numero) - 1
    decimal = 0
    
    for x in numero:
        decimal += int(x) * 2 ** expo
        expo -= 1
    
    return decimal

def a_binario(decimal):
    
    binario = ""
    
    while decimal > 0:
        
        resto = decimal % 2
        binario = str(resto) + binario
        decimal = decimal // 2
    
    return binario

def limpia():
    print "-" * 29
    print
    raw_input("'Enter' para continuar.")
    import os    
    os.system('clear')

main()
