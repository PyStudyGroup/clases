#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 15/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Unidad 4 - Desafío 1

# Una funcion que reciba un array (de lo que sea) y devuelva un array 
# sin repeticiones.

def main():
    
    print "Escriba una secuencia de caracteres numéricos y alfanuméricos. \n"
    secuencia = raw_input("Secuencia: ")
    
    print "Caracteres únicos:", norepet(secuencia)
    
def norepet(secuencia):
    
    lista = ""
    
    for x in secuencia:
        if x not in lista:
            lista += x
    
    return lista
        
main()
