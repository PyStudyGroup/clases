# -*- coding: utf-8 -*-

tlibros = input("Total de libros")
taza = input("Taza:")

taza /= 100.00

total = 0.0
impuestos = 0.0
titulos = ""

for i in range(tlibros):
    nom = input("Titulo")
    precio = input("Precio:")
    titulos += nom + "\t $" + str(precio) + "\n"
    total += precio

impuestos = total * taza
print "-" * 30
print "Libro\tCosto"
print titulos
print "Subtotal:\t" + str(total)
print "impuesto:\t" + str(impuestos)
print "Total:\t" + str(total + impuestos)



