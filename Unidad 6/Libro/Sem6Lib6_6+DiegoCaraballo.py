#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Diego Caraballo
# @date: 26/05/13
# @version: python 2.7.4
# Grupo Estudio Python


"""Ejercicio 6.6. Escribir un programa que cuente cúantas 
veces aparecen cada una de las vocales en una cadena. No importa 
si la vocal aparece en mayúscula o en minúscula."""

def main():
	print "Ingresa una cadena de texto: "
	texto = raw_input()
	print contar_vocales (texto)

def contar_vocales (cadena):
	contadora = 0
	contadore = 0
	contadori = 0
	contadoro = 0
	contadoru = 0
	for x in cadena:
		if x == "a" or x == "A":
			contadora += 1
		elif x == "e" or x == "E":
			contadore += 1
		elif x == "i" or x == "I":
			contadori += 1
		elif x == "o" or x == "O":
			contadoro += 1
		elif x == "u" or x == "U":
			contadoru += 1
	print "Hay", contadora, "letras a"
	print "Hay", contadore, "letras e"
	print "Hay", contadori, "letras i"
	print "Hay", contadoro, "letras o"
	print "Hay", contadoru, "letras u"
	
main()
