# -*- coding: utf-8 -*-
"""
Created on Thu May 16 03:21:30 2013

@author: cllamach
"""

#Desafio 4 - Semana 4

"""
Realiza un programa que calcule el desglose en billetes y
monedas de una cantidad exacta de euros. Hay billetes 
de 500, 200, 100, 50, 20, 10 y 5 euros y
monedas de 2 y 1 euro. Por ejemplo, si deseamos conocer 
el desglose de 434 euros, el programa mostrará por pantalla 
el siguiente resultado:
     
2 billetes de 200 euros.

1 billete de 20 euros.

1 billete de 10 euros.

2 monedas de 2 euros.
     
"""

def desglose(dinero):
    
    de500 = 0
    de200 = 0
    de100 = 0
    de50 = 0
    de20 = 0
    de10 = 0
    de5 = 0
    de2 = 0
    de1 = 0
    
    original = dinero
    
    while dinero != 0:
        
        if dinero % 500 != dinero:
            dinero = dinero - 500
            de500 +=1
        elif dinero % 200 != dinero:
            dinero = dinero - 200
            de200+=1
        elif dinero % 100 != dinero:
            dinero = dinero - 100
            de100 += 1
        elif dinero % 50 != dinero:
            dinero = dinero - 50
            de50+= 1
        elif dinero % 20 != dinero:
            dinero = dinero - 20
            de20 += 1
        elif dinero % 10 != dinero:
            dinero = dinero - 10
            de10 += 1
        elif dinero % 5 != dinero:
            dinero = dinero - 5
            de5+= 1
        elif dinero == 1:
            de1 += 1
            dinero -=1
        elif dinero % 2 != dinero:
            dinero = dinero - 2
            de2 +=1
            
    print("{0} de 500, {1} de 200, {2} de 100, {3} de 50, {4} de 20, {5} de 10, {5} de 10, {6} de 5, {7} de 2, {8} de 1 que suman {9}".format(de500, de200, de100, de50, de20, de10, de5, de2, de1, original))            
    
if __name__=="__main__":
    desglose(426)
    desglose(232)
    desglose(132)
    desglose(345)
    desglose(1132)
                
        
            
        
        