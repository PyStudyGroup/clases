#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Diego Caraballo
# @date: 10/05/13
# @version: python 2.7.4
# Grupo Estudio Python

"""Ejercicio 4.3. Dados tres puntos en el plano expresados como coordenadas (x, y) informar cuál
es el que se encuentra más lejos del centro de coordenadas."""


from math import sqrt

def main():
	print "Ingresa 3 puntos para saber cual esta mas lejos del centro de coordenadas"
	print "Coordenadas (x, y) del punto 1:"
	xp1 = input ("Coordenada x: ")
	yp1 = input ("Coordenada y: ")
	print "Coordenadas (x, y) del punto 2:"
	xp2 = input ("Coordenada x: ")
	yp2 = input ("Coordenada y: ")
	print "Coordenadas (x, y) del punto 3:"
	xp3 = input ("Coordenada x: ")
	yp3 = input ("Coordenada y: ")

#((x2-x1)**2) + ((y2-y1)**2)) Formula para saber la distancia entre dos puntos
# En este caso x1, y1 es 0, 0

	punto1 = mas_cerca (xp1, yp1)
	punto2 = mas_cerca (xp2, yp2)
	punto3 = mas_cerca (xp3, yp3)

	if punto1 == punto2 and punto1 == punto3:
		print "Los 3 puntos tienen la misma distancia al punto (0, 0)"
	elif punto1 == punto2 or punto1 == punto3 or punto2 == punto3:
		print "Dos de los puntos tienen la misma distancia con respecto a (0, 0)"
		if punto1 == punto2 and punto1 < punto3:
			print "Punto 1 y punto 2 estan mas cerca del origen"
		elif punto1 == punto3 and punto1 < punto2:
			print "Punto 1 y punto 3 estan mas cerca del origen"
		elif punto2 == punto3 and punto2 < punto1:
			print "Punto 2 y punto 3 estan mas cerca del origen"
		else: 
			if punto1 == punto2 and punto1 > punto3:
				print "El punto 3 esta mas cerca del origen"
			elif punto1 == punto3 and punto1 > punto2:
				print "El punto 2 esta mas cerca del origen"
			elif punto2 == punto3 and punto2 > punto1:
				print "El punto 1 esta mas cerca del origen"
	else:
		if punto1 < punto2 and punto1 < punto3:
			print "El punto mas cerca es: ", punto1
		elif punto2 < punto1 and punto2 < punto3:
			print "El punto mas cerca es: ", punto2
		else:
			print "El punto mas cerca es: ", punto3


def mas_cerca (x2, y2): #La funcion determina la distancia entre el punto y el origen
	x1 = 0
	y1 = 0
	d = sqrt( ((x2-x1)**2) + ((y2-y1)**2))
	return d
	
main()
	
