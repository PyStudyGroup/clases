#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Diego Caraballo
# @date: 10/05/13
# @version: python 2.7.4
# Grupo Estudio Python


"""Escriba un programa que pida un año y que escriba si es bisiesto o no. 
Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos
de 100 no lo son, aunque los múltiplos de 400 sí.
Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 
no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto."""

def main():
	print "Comprobador de años bisiestos"
	a = input ("Escriba un años y le dire si es bisiesto: ")
	if a % 4 == 0 and (not(a % 100 == 0)):
		print "El año", a, "es un año bisiesto porque es multiplo de 4"
	elif a % 400 == 0:
		print "El año", a, "es un año bisiesto porque es multiplo de 400"
	else:
		print "El año", a, "no es bisiesto"
	

main()
	
