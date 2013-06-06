#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Diego Caraballo
# @date: 10/05/13
# @version: python 2.7.4
# Grupo Estudio Python


"""Escriba un programa que pida los coeficientes de una ecuación de 
primer grado (a x + b = 0) y escriba la solución. 
Se recuerda que una ecuación de primer grado puede no tener solución,
tener una solución única, o que todos los números sean solución. 
Se recuerda que la fórmula de las soluciones es x = -b / a"""

def main():
	print "Ecuacion ax + b = 0"
	a = input ("Escriba el valor del coeficiente a: ")
	b = input ("Escriba el valor del coeficiente b: ")
	if a == 0 and b == 0:
		print "Todos los numeros son solucion"
	elif a == 0:
		print "Sin solucion"
	else:
		print "La solucion de la ecuacion es: ", resultado (a, b)
	
def resultado (x, y):
	x = float (x)
	y = float (y)
	resul = -y / x
	return resul
	
main()
