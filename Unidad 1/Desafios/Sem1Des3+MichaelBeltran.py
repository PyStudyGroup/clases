#!/usr/bin/ python
#-*- encoding: utf-8 -*-
'''
Created on 24/04/2013

@author: michael
'''
def cua(m,t):
    fil=[]
    for i in range(m-t):
        fil.append("    ")
    for i in range(t):
        fil.append("____")
    return fil
def barras():
    #ban=True
    #while ban:
    maxi=input("tamaño maximo: ")
    b1=input("tamaño de la primera barra: ")
    b2=input("tamaño de la segunda barra: ")
    b3=input("tamaño de la tercera barra: ")
    b4=input("tamaño de la cuarta barra: ")
    '''if ba1>cuadro or ba2>cuadro or ba3>cuadro or ba4>cuadro:
        print("El Tamaño de alguna de las barras es mayor que el maximo permitido")
        ban=True
    else:
         ban=False'''
    
    # "+ ____ ____ ____ ____ +"
    print "+"*23
    b1=cua(maxi,b1)
    b2=cua(maxi,b2)
    b3=cua(maxi,b3)
    b4=cua(maxi,b4)
    
    for i in range(maxi):
        print "+",
        print b1[i],b2[i],b3[i],b4[i],"+"       
    print "+  b1   b2   b3   b4  +"
    print "+"*23

barras()