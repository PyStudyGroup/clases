#!/usr/bin/env python3


from subprocess import call
from textwrap import dedent
from time import sleep
import sys


def es_valido(s):
    try:
        float(s)
    except ValueError:
        print("ERROR! La cadena: '%s', NO es una expresion valida, para numeros flotantes." % s)
    else:
        print("La cadena: '%s', es una expresion valida, para numeros flotantes." % s)
  


def main():
    while True:
        call('clear')
        cadena_in = input(dedent('''\
                                     Escriba una expresion para numeros flotantes, 
                                     su validez sera evaluada: (S/SALIR, para finalizar)
                                     => '''))
        if cadena_in.lower() in ['s', 'salir']:
            sys.exit()
        else:
            es_valido(cadena_in)
            sleep(5)
  
  
  
if __name__ == '__main__':
    main()
