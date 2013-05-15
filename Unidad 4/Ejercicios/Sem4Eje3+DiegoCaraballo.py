#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Diego Caraballo
# @date: 10/05/13
# @version: python 2.7.4
# Grupo Estudio Python

"""Escriba un programa que pida el año actual y un año cualquiera y 
que escriba cuántos años han pasado desde ese año o cuántos años 
faltan para llegar a ese año."""

def main():
	print "Comparador de años"
	actual = input ("En que año estamos?: ")
	cualquiera = input ("Escriba un año cualquiera: ")
	x = diferencia (actual, cualquiera)
	if x == 0:
		print "Son el mismo año"
	elif x == 1:
		print "Para llegar al", (cualquiera + 1), "falta 1 año"
	elif x > 0:
		print "Para llegar al año", cualquiera, "faltan", x, "años"
	elif x < 0:
		print "Dese el año", cualquiera, "han pasado", (-x), "años"
	
	
def diferencia (a1, a2):
	dif = a2 - a1
	return dif


main()
