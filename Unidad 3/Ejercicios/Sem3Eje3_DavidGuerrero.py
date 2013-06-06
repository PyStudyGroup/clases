#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 06/05/2013
@author: DeivGuerrero
'''

def suma_digitos(num):
    """Retorna la suma de todos los 
    digitos de <num>"""
    n = 0
    #Recorremos <num> como string
    for d in str(num):
        #Sumanos y asignamos a <n> el valor de <d>
        n += int(d)
    return n


#Imprimimos lo que la <suma_digitos> retorna, y le pasamos
#como parametro lo que el input retorna
print suma_digitos(input("Introduce un numero:"))