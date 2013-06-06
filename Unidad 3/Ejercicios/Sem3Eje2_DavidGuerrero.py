#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 06/05/2013
@author: DeivGuerrero
'''

def funcionRara(a, b, c, d):
    """Retorna una tupla con los resultados"""
    return (a*b, c/d, b-c)


#Solicitamos los valor al usuario
a = input ("1er Valor:")
b = input ("2do Valor:")
c = input ("3er Valor:")
d = input ("4to Valor:")


#Imprimimos el resultado que retorna la funcion
print funcionRara(a, b, c, d)