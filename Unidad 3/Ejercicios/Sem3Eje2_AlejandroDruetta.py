#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Semana 3 - Ejercicio 2

# Hacer un método que reciba cuatro parámetros, y devuelve el primero 
# por el segundo, el tercero entre el cuarto, y el segundo menos el 
# tercero.

def main():
	
	def funcioRara(p1, p2, p3, p4):
		
		calculo1 = p1 * p2
		calculo2 = p3 * p4
		calculo3 = p2 - p3
		
		return calculo1, calculo2, calculo3

main()
	
