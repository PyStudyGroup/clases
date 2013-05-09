#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Unidad 3 - Libro 3.2


def main():
	
	repite_hola(3)
	repite_hola(5)
	repite_hola(7)

def repite_hola(n):
	""" Recibe como parámetro un número entero 'n' y la cadena formada 
		por n concatenaciones de 'Hola'. """
	
	print "-" * 5 * n
	print "repite_hola(" + str(n) + ")"
	print "-" * 5 * n
	print "Hola!" * n
	print ""
	
main()
