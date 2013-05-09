#!/usr/bin/python
#-*- encoding: utf-8 -*-
'''
Created on 2/05/2013

@author: michael
'''
def conversor():
    b=raw_input("digite su numero binario > ")
    print b,"en base decimal es ",nb(b)
    
def nb(bi):#la funcion es hacer los calculos de convercion
    r=0
    c=0
    ca=len(bi)-1#se resta 1 para que no desborde el string 
    #ejemplo si len(bi) es 5 el tamaño de bi enrealidad es 4 0,1,2,3,4 
    for i in range(ca,-1,-1):#-1equibale ala primera pocision de bi       
        n=2**c#a "n" se eleva a la potencia que "c" tenga en el momento
        r+=n*int(bi[i])
        c+=1
    return r
conversor()