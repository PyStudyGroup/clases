#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Diego Caraballo
# @date: 26/05/13
# @version: python 2.7.4
# Grupo Estudio Python

"""Ejercicio 6.4. Escribir una función contar(l, x) que cuente 
cuántas veces aparece un carácter l dado en una cadena x."""

def contar1 (cadena):
	contador = 0
	for x in cadena:
		if x == "1":
			contador += 1
	return contador
	
print contar1 ("die1dal1dajdñk111lkjasd")	
