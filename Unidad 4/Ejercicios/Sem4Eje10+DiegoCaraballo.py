#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Diego Caraballo
# @date: 12/05/13
# @version: python 2.7.4
# Grupo Estudio Python

"""Escriba un programa que pida una distancia en centímetros y que escriba 
esa distancia en kilómetros, metros y centímetros (escribiendo solamente 
las unidades necesarias).

La dificultad del ejercicio se puede reducir o aumentar según la forma de 
presentar el resultado:
sin separador entre unidades: 2 km 400 m 5 cm 
separando con comas las unidades: 2 km, 400 m, 5 cm 
separando con comas y con la conjunción 'y' en la 
última unidad: 2 km, 400 m y 5 cm"""

def main():
	print "Convertidor de centimetros a kilometros, metros y centimetros"
	x = input ("Escriba una distancia en centimetros: ")
	print ""
	if x < 100:
		print "Los centimetros no alcanzan un metro, por lo tanto son", x, "cm"
	elif x < 100000:
		metros = a_metros (x)
		centimetros = x % 100
		if centimetros != 0:
			print x, "centimetros son", metros, "m y", centimetros, "cm"
		else:
			print x, "centimetros son", metros, "m"
	elif x >= 100000:
		kilometros = a_kilometros (x)
		metros = a_metros (x % 100000)
		centimetros = (x % 100000) % 100
		if metros != 0 and centimetros != 0:
			print x, "centimetros son", kilometros, "km,", metros, "m y", centimetros, "cm"
		elif metros != 0 and centimetros == 0:
			print x, "centimetros son", kilometros, "km y", metros, "m"
		elif metros == 0 and centimetros != 0:
			print x, "centimetros son", kilometros, "km y", centimetros, "cm"
		else:
			print x, "centimetros son", kilometros, "km"
	else:
		print "Opcion equivocada, intente una ves mas..."
		print ""
		main()
	
	
def a_metros (a):
	metros = a / 100
	return metros
	
def a_kilometros (a):
	kilometros = a / 100000
	return kilometros
	
main()

