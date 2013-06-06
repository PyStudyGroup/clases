'''
Created on 23/04/2013

@author: michael
'''

def inter():
    numero = input("ingrese un numero entero> ")
    print numero
    conta = 0
    for i in range(1,numero):
        numero+=conta
        print numero
        conta+=1
        
inter()       
        