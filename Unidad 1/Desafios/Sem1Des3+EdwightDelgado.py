#coding:utf-8

maximo = input("Tamaño maximo: ")
barra1 = input("Tamaño de barra1: ")
barra2 = input("Tamaño de barra2: ")
barra3 = input("Tamaño de barra3: ")
barra4 = input("Tamaño de barra4: ")

barra = "____"
espacio = " " * 6


print ""
print "El maximo alcance de la barra es: ", maximo

print "+" * 20

for x in range(maximo):

    contador = maximo - x

    if barra1 < contador:
        b1 = espacio

    else:
        b1 = barra

    if barra2 < contador:
        b2 = espacio
    else:
        b2 = barra
    if barra3 < contador:

        b3 = espacio
    else:
        b3 = barra
    if barra4 < contador:
        b4 = espacio
    else:
        b4 = barra

    print " + ", b1, b2, b3, b4, "  +  "

print "+   b1   b2   b3   b4   +"
print "+" * 20


