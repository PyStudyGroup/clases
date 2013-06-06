#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main():
	""" Dibuja cuatro barras y un marco, ingresando los cuatro 
	valores de las barras y el límite máximo. """
	
	max = input("Tamanho maximo: ")
	
	bar1 = input("Tamaño de barra1: ")
	bar2 = input("Tamaño de barra2: ")
	bar3 = input("Tamaño de barra3: ")
	bar4 = input("Tamaño de barra4: ")
	
	bar_vacia = " " * 4
	bar_llena = "_" * 4
	
	print ""
	print "El maximo alcance de la barra es: ", max
	
	print "+" * 23
	
	for x in range(max):
		
		cont = max - x
		
		if bar1 < cont:
			b1 = bar_vacia
		else:
			b1 = bar_llena
		if bar2 < cont:
			b2 = bar_vacia
		else:
			b2 = bar_llena
		if bar3 < cont:
			b3 = bar_vacia
		else:
			b3 = bar_llena
		if bar4 < cont:
			b4 = bar_vacia
		else:
			b4 = bar_llena
		
		print "+", b1, b2, b3, b4, "+"
		
	print "+  b1   b2   b3   b4  +"
	print "+" * 23

main()
