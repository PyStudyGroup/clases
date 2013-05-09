#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Unidad 3 - Libro 3.5

def main():
		
	for x in range(3):
		
		h = input("Cuántas horas? ")
		m = input("Cuántos minutos? ")
		s = input("Cuántos segundos? ")
		
		mensaje = "Son " + str(calc_asegundos(h, m, s)) + " segundos."
		
		print ""
		print "-" * len(mensaje)
		print mensaje
		print "-" * len(mensaje)
		print ""

def calc_asegundos(horas, minutos, segundos):
		""" Transforma en segundos una medida de tiempo expresada en
			horas, minutos y segundos """
		
		segsal = 3600 * horas + 60 * minutos + segundos # regla de transformacion
		return segsal

main()
