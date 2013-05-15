#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Diego Caraballo
# @date: 10/05/13
# @version: python 2.7.4
# Grupo Estudio Python

"""Escriba un programa que pida dos números enteros y
 que escriba si el mayor es múltiplo del menor."""
 
def main():
	print "Comparador de multiplos"
	n1 = input("Ingresa un numero entero: ")
	n2 = input("Ahora otro numero entero: ")
	comparador = es_multiplo(n1, n2)
	print comparador
	
	
def es_multiplo (x1, x2):
	if x1 > x2:
		resto = x1 % x2
		if resto == 0:
			print x1, "es multiplo de", x2
		else:
			print x1, "no es multiplo de", x2
	else:
		resto = x2 % x1
		if resto == 0:
			print x2, "es multiplo de", x1
		else:
			print x2, "no es multiplo de", x1


main()
