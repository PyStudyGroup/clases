#!/usr/bin/env python
# -*- coding: utf-8 -*-

suma, numero = 0, input("Digite número: ")
print numero
for i in range(numero - 1):
    numero += suma
    print numero
    suma += 1
