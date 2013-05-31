#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Diego Caraballo
# @date: 26/05/13
# @version: python 2.7.4
# Grupo Estudio Python

"""Ejercicio 6.1. Escribir un ciclo que permita mostrar los caracteres
de una cadena del final al principio."""

def cadena(texto):
	"""Cadena que imprime en pantalla el texto invertido"""
	s = -len (texto)
	indice = -1
	while indice >= s:
		print texto[indice]
		indice = indice + (-1)
	
		
print cadena ("Este es el ejercicio 6.1")
