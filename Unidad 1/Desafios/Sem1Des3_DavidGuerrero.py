#! /usr/bin/env python
# -*- coding: utf-8 -*-
max = input("Tamanho maximo:")
tb1 = input("Tamanho de barra1:")
tb2 = input("Tamanho de barra2:")
tb3 = input("Tamanho de barra3:")
tb4 = input("Tamanho de barra4:")
 
print "+" * 23
salida = ""

"""usamos la forma completa del range para indicar
que queremos de mayor a menor range(inicio, tope, salto)
"""

for c in range(max, 0, -1):
    salida = "+ "
    if tb1 >= c:
        salida += "_" * 4 + " "
    else:
        salida += " " * 4 + " "
    
    if tb2 >= c:
        salida += "_" * 4 + " "
    else:
        salida += " " * 4 + " "
        
    if tb3 >= c:
        salida += "_" * 4 + " "
    else:
        salida += " " * 4 + " "
    
    if tb4 >= c:
        salida += "_" * 4 + " "
    else:
        salida += " " * 4 + " "
    salida += "+"
    print salida

print "+  b1   b2   b3   b4  +"
print "+" * 23
        
        