#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Semana 5 - Desafío 2
# Autor:    Alejandro Druetta
# Fecha:    22/05/13

def main():
    
    limite = int(raw_input("Digite el número límite de la sucesión: "))
    sucesion(limite)
    
def sucesion(limite):
    
    num1 = 0
    num2 = 1
    numero = 0
    
    print num1
    print num2
    
    while True:
        numero = num1 + num2
        if numero > limite:
            break
        else:
            print numero
        
        num1 = num2
        num2 = numero        
    
main()
