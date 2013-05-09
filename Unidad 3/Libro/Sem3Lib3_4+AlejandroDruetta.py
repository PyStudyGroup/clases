#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Unidad 3 - Libro 3.4

def main():

	print repite_saludo("Hola, qué tal? ", 3)
	print repite_saludo("Cómo estás? ", 5)
	print repite_saludo("Buenos días! ", 7)

def repite_saludo(saludo, n):
	""" Recibe como parámetro un número entero n y una cadena saludo y 
		retorna el valor de n concatenaciones de saludo. """
	
	concat = saludo * n
	print ""

	return concat

main()
