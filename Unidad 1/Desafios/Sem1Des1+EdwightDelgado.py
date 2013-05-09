#coding:utf-8
"""
escriba un pequño programa donde:
- se ingrese el año en curso
- se ingrese el nombre y el año de nacimiento de tres personas.
se calcula cuantos años cumplira en el año en curso
"""

print "BIENVENIDOS"
for x in range(3):
    a_curso = raw_input("ingrese el año en curso: ")
    a_nacimiento = raw_input("ingrese el año de nacimiento: ")
    nombre = raw_input("ingrese su nombre: ")
    edad = int(a_curso) - int(a_nacimiento)
    print nombre + " " + "usted cumplira %s" %edad + " años de edad"


