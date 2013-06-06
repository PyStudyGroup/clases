#!/usr/bin/env python
#-*- coding: utf-8 -*-

n = int(raw_input("Dame un numero: "))

a = range(1, n+1)
a.extend(range(n-1, 0, -1))

for i in a:
    s = " " * (n - i)
    b = range(1, i+1)
    b.extend(range(i-1, 0, -1))
    
    for j in b:
        s += str(j)
    s += " " * (n - i)
    print s