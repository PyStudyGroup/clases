#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Diego Caraballo
# @date: 10/05/13
# @version: python 2.7.4
# Grupo Estudio Python


"""Escriba un programa que pida tres números y que escriba 
si son los tres iguales, si hay dos iguales o si son los tres distintos."""

def main():
	print "Comparador de 3 numeros"
	n1 = input ("Escriba un numero: ")
	n2 = input ("Escriba otro numero: ")
	n3 = input ("Escriba otro numero mas: ")
	if n1 == n2 and n1 == n3:
		print "Has escrito tres veces el mismo numero"
	elif n1 == n2 or n1 == n3 or n2 == n3:
		print "Has escrito uno de los numeros dos veces"
	else:
		print "Los tres numeros que ha escrito son distintos"
		
main()

