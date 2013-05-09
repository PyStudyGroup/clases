#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Semana 3 - Ejercicio 4

# Hacer un metodo que recibe un numero entero mayor o igual que 1 y 
# devuelve el factorial (la multiplicacion desde 1 hasta el mismo 
# numero)

def main():
	
	entrada = input("Ingrese un número mayor o igual que 1: ")
	print "El factorial de", entrada, "es:", factorial(entrada)
	
def factorial(numero):
	
	fac = 1
	numero += 1
	
	for x in range(2, numero):
		fac *= x
	
	return fac
	
main()
