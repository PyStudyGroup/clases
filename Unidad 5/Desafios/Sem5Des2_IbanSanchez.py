#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Ibán Sánchez

limite = int(raw_input("introduce hasta que numero quieres la secuencia:  "))

def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b
     
for n in fibonacci(limite):
    print(n)