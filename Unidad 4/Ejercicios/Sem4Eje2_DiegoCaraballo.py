#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Diego Caraballo
# @date: 10/05/13
# @version: python 2.7.4
# Grupo Estudio Python

"""Escriba un programa que pida dos números y que conteste cuál
 es el menor y cuál el mayor o que escriba que son iguales."""
 
def main():
	 print "Comparador de numeros"
	 n1 = input ("Ingresa un numero: ")
	 n2 = input ("Ahora otro: ")
	 
	 if n1 == n2:
		 print "Los dos numeros son iguales"
	 elif n1 > n2:
		 print "Menor:", n2, "; Mayor:", n1
	 elif n2 > n1:
		 print "Menor:", n1, "; Mayor:", n2
		 
main()
