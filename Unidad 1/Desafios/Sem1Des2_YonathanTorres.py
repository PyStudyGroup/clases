#! /usr/bin/env python2

nro = int(raw_input('Ingrese un numero entero: '))
print nro
for i in range(nro-1):
	nro += i
	print nro
