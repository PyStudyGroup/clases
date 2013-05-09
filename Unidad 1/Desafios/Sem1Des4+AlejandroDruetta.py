#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main():
	
	n = input("Dame un número: ")
	base = 0
	numero = 0
	
	for x in range(n):
		base = "1" + (x * "2") + (x * "0")
		numero += int(base)
		blanco = " " * (n - x)
		print blanco + str(numero) + blanco
		
	n -= 1
		
	for y in range(n, 0,  -1):
		base = "1" + (y * "2") + (y * "0")
		numero -= int(base)
		blanco = " " * (n - y + 2)
		print blanco + str(numero) + blanco
	
main()
