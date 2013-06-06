#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Unidad 3 - Libro 3.3

def main():
		
	repite_saludo("Hola, qué tal? ", 3)
	repite_saludo("Buenos días! ", 5)
	repite_saludo("Cómo andás? ", 7)

def repite_saludo(saludo, n):
	""" Recibe como parámetro un número entero n y una cadena saludo y 
		escribe por pantalla el valor de saludo n veces."""
	
	print "-" * 15
	print "repite_hola(" + str(n) + ")"
	print "-" * 15
	
	for x in range(n):
		print saludo
	
	print ""

main()
