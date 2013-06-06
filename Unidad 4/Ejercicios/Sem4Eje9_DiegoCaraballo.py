#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Diego Caraballo
# @date: 12/05/13
# @version: python 2.7.4
# Grupo Estudio Python

"""Escriba un programa que pregunte primero si se quiere calcular el 
área de un triángulo o la de un círculo. Si se contesta que se quiere 
calcular el área de un triángulo, el programa tiene que pedir entonces 
la base y la altura y escribir el área. Si se contesta que se quiere 
calcular el área de un círculo, el programa tiene que pedir entonces 
el radio y escribir el área.
Se recuerda que el área de un triángulo es base por altura dividido por 
2 y que el área de un círculo es Pi (aproximadamente 3,141592) por 
el radio al cuadrado."""

def main():
	print "Calculo de areas - Elija una figura geometrica"
	print "a) Triangulo"
	print "b) Circulo"
	print ""
	x = raw_input ("Que figura quiere calcular (Escriba T o C)? ")
	if x == "T" or x == "t":
		base = input ("Escriba la base: ")
		altura = input ("Escriba la altura: ")
		area = area_triangulo (base, altura)
		print "Un triangulo de base", base, "y altura", altura, "tiene un area de", area
	elif x == "C" or x == "c":
		radio = input ("Escriba el radio: ")
		area = area_circulo (radio)
		print "Un circulo de radio", radio, "tiene un area de", area
	else:
		print "Opcion incorrecta, vuelva a intentarlo"
		print ""
		main()

def area_circulo (a):
	Pi = 3.141592
	area = Pi * (a*a)
	return area	
		
def area_triangulo (a, b):
	area = (a * b) / 2
	return area
	

main()



