#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Unidad 3 - Libro 3.1

def main():

	repite_hola(3)
	repite_hola(5)
	repite_hola(7)

def repite_hola(n):
	""" Recibe como parámetro un número entero 'n' y escribe en 
		pantalla 'Hola' n veces. """
	
	print "-" * 15
	print "repite_hola(" + str(n) + ")"
	print "-" * 15

	for x in range(n):
		print "Hola!"

main()
