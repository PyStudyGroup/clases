#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Diego Caraballo
# @date: 12/05/13
# @version: python 2.7.4
# Grupo Estudio Python

"""Escriba un programa que pida los coeficientes de una ecuación de 
segundo grado (a x² + b x + c = 0) y escriba la solución. 
Se recuerda que una ecuación de segundo grado puede no tener solución, 
tener una solución única, tener dos soluciones o que todos los números 
sean solución. Se recuerda que la fórmula de las soluciones cuando hay 
dos soluciones es x = (-b ± √(b2-4ac) ) / (2a)"""

from math import sqrt #Se utiliza para calcular raiz cuadrada
#(-b ± √(b2-4ac) ) / (2a)
def main():
	print "Ecuacion ax² + bx + c = 0"
	n1 = input ("Escriba el valor del coeficiente a: ")
	n2 = input ("Escriba el valor del coeficiente b: ")
	n3 = input ("Escriba el valor del coeficiente c: ")
	if n1 == 0:
		n2 = float(n2)
		n3 = float(n3)
		z = -n3/n2
		print "Una solucion: ", z
	elif ((n2*n2) - (4*n1*n3)) < 0:
		print "Sin solucion real"
	elif n1 == 0 and n2 == 0 and n3 == 0:
		print "Todos los numeros son solucion"
	elif n1 == 0 and n2 == 0:
		print "Sin solucion"
	else: 
		x = ecuacion_x (n1, n2, n3)
		y = ecuacion_y (n1, n2, n3)
		if x == y:
			print "Una solucion: ", x
		elif x != y:
			print "Dos soluciones: ", x, "y", y
		
	
	
#(-b ± √(b2-4ac) ) / (2a)
	
def ecuacion_x (a, b, c): #Me salioooooooooooooooooo
	x = ((-b + sqrt((b*b) - (4*a*c))) / (2*a))
	return x

def ecuacion_y (a, b, c):
	y = ((-b - sqrt((b*b) - (4*a*c))) / (2*a))
	return y


main()
