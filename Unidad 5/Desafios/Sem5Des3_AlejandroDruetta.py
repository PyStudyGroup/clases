#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Semana 5 - Desafío 3
# Autor:    Alejandro Druetta
# Fecha:    22/05/13

def main():
    
    cantidad = int(raw_input("Digite la cantidad de números fibonacci que quiere: "))
    sucesion(cantidad)
    
def sucesion(cantidad):
    
    num1 = 0
    num2 = 1
    numero = 0
    
    print num1
    print num2
    
    for x in range(cantidad - 2):
        numero = num1 + num2
        print numero        
        num1 = num2
        num2 = numero        
    
main()
