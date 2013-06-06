# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Python v3.3

# Introducimos el % de impuesto y el numero de libros comprados
impuesto = float(input("Impuesto aplicable: "))
numero = int(input("Cuantos libros compraste?: "))

# Defino dos listas, una para el titulo del libro y otra para el precio
libro = []
precio = []

# funcion que me va pidiendo los datos de titulo y precio
# del total de libros comprados y los añade a la lista de libro y precio
def rellena_datos(num):
    for i in range(0,num):
        libro.append(input("Introduce el titulo del libro: "))
        precio.append(float(input("Introduce su precio: ")))
   

# funcion que me suma el precio de los libros para darme la Base del precio
def suma():
	sumatorio = 0
	for i in precio:
		sumatorio += float(i)
	return sumatorio


# funcion para dar el formato de salida estilo ticket de compra	
def formato(nombre, num):
		if len(nombre)>10: #si el titulo es de mas de 10 caracteres
			titulo=nombre[0:10] #me quedo con los 10 primeros
			print (titulo + " " * (10-(len(str(num)))) ,num)
		else: # si es menor de 10 caracteres relleno con espacios
			print(nombre + " " * (20 - (len(nombre) + len(str(num)))) ,num)
		

rellena_datos(numero)

print("-"*22)

for i in range(0,numero):
    formato(libro[i], precio[i])
    
print("-"*22)
base = round(float(suma()),2) # redondeo el precio Base con 2 decimales, el float a lo mejor no es necesario
print("Base " + " "*10, base)
iva = round((base * impuesto / 100),2) # calculo el impuesto y redondeo a 2 decimales
print("IVA   " + " "*10, iva)
print("-"*22)
total = round((base + iva),2) # calculo el precio total y redondeo con 2 decimales
print("Total" + " "*10, total)
