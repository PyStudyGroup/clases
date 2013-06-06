#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 06/05/2013
@author: DeivGuerrero
'''

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

print factorial(input("Introduce un numero:"))