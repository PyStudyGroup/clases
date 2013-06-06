#!/usr/bin/env python
# -*- encoding: utf-8 -*-
def main():
    anyo=input("Ingrese el año en curso: ")
    print "Ingrese el nombre y el año de nacimiento de tres personas"
    n1 = raw_input("nombre 1ra persona: ")
    p1 = input("¿en que año nacio ?> ")
    n2 = raw_input("nombre 2da persona: ")
    p2 = input("¿en que año nacio ?> ")
    n3 = raw_input("nombre 3ra persona: ")
    p3 = input("¿en que año nacio ?> ")
    print "***********************"
    print n1,"tiene",anyo-p1,"años"
    print n2,"tiene",anyo-p2,"años"
    print n3,"tiene",anyo-p3,"años"

main()
    