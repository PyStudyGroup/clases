#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Programa:     Sem4Des4+AlejandroDruetta.py
# Propósito:    Realizar el desglose en billetes y monedas.

# Autor:        Alejandro Druetta
# Fecha:        15/05/13
# Versión:      Python 2.7.4

def main():
    
    dinero = int(raw_input("Ingrese un valor en euros: "))
    
    b = "billetes"
    m = "monedas"
    valor = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    tipo = [b, b, b, b, b, b, b, m, m]
    
    for x in range(9):
                
        if dinero >= valor[x]:
            print dinero // valor[x],
            print tipo[x], "de",
            print valor[x], "euros."
            dinero %= valor[x]
            
main()