#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Semana 5 - Desafío 4
# Fecha:    23/05/13
# Autor:    Alejandro Druetta

def main():
    
    impar = int(raw_input("Escriba un número impar mayor que 5: "))
    print
    primos = listar_primos(impar)
    print "Números primos entre 2 y %d:" % impar, primos
    
    triadas = []
       
    for x in primos:                                        # Prueba todas las combinaciones de suma.
        for y in primos:
            for z in primos:
                if (x + y + z) == impar:
                    triada = [x, y, z]
                    triada_ordenada = ordena(triada)
                    if triada_ordenada not in triadas:      # Si no se repite, la agrega a la lista.
                        triadas.append(triada_ordenada)
    
    print
    for i in range(len(triadas)):
        for ii in range(3):
            print triadas[i][ii] ,
            if ii < 2:
                print "+" ,
        print "= %d \n" % impar

def ordena(triada):
    """Ordena las triadas de menor a mayor para poder eliminar las que\
       se repiten"""
    
    for x in range(3):
        for y in range(3):
        
            if triada[x] < triada[y]:
                temp = triada[x]
                triada[x] = triada[y]
                triada[y] = temp
    
    return triada
   
    
def listar_primos(impar):
    """Recibe un número impar mayor que 5 y determina todos los primos\
       comprendidos entre 2 y ese número"""
    
    primos = [2, 3, 5]                                  # Como el impar debe ser mayor que 5, los primeros primos ya los conocemos.
        
    for numero in range(7, impar, 2):                   # Recorre todos los impares entre el 7 y el anterior a 'impar'.
        control = 1
        maximo = numero // 2                            # Los números mayores a 'maximo' no cuentan porque nunca darán resto 0.
        
        for divisor in range(2, maximo):
            resto = numero % divisor
            control *= resto                            # Si en algún momento 'resto' es igual a 0, control valdrá 0 a partir de ahí.
        
        if control != 0:
            primos.append(numero)
    
    return primos
    
main()
