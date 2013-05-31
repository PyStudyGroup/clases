#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Diego Caraballo
# @date: 26/05/13
# @version: python 2.7.4
# Grupo Estudio Python

"""Ejercicio 6.5. ¿Hay más letras “A” o más letras “E” en una cadena?
Escribir un programa que lo decida."""

def contar_letra (cadena):
	contador = 0
	print "Que letra quieres contar?"
	letra = raw_input()
	for x in cadena:
		if x == letra:
			contador += 1
	if contador > 0:
		print "Se termino la busqueda de letras", letra
		return contador
	else:
		print "No existe la letra", letra, "en esta cadena"
	
print contar_letra ("diego caraballo")
