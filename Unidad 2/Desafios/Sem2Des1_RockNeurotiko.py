#!/usr/bin/python
#-*- encoding: utf-8 -*-
''' 
@author: Rock Neurotiko
'''

def aDecimal(numeroBin):
    decimal = 0 #El numero final
    exp = len(numeroBin) -1 #El exponente al que elevar 2
    for i in numeroBin: #Recorremos el numero
        decimal += (int(i) * 2**(exp)) #Calculamos el valor a incrementar
        exp = exp-1 #Disminuimos el exponente
    return decimal


def main():
    while(True):
        numeroBin = raw_input("Numero binario: ")
        #Esta hecho para Python 2.7, si se ejecuta en 3.x
        #deberia ser input() y habia que castearlo a un str
        print "%s = %s" %(numeroBin, aDecimal(numeroBin))


if __name__ == "__main__":
    main()
