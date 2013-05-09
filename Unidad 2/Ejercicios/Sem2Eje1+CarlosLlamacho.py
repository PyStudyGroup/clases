#Semana 2 - Unidad 2
#Ejercicio 1

"""Nivel de dificultad: Media (en relación al nivel de la unidad)

Escribir un programa que calcule el costo total de una
compra de libros. Primero pregunta la cantidad de libros
y la taza de impuestos. Luego pregunta el título y el precio
de cada libro. Finalmente, imprime el número de libros, la
suma del valor de los libros, el valor de los impuestos y el total a pagar."""

cant_libros = int(input("Cuantos libros quiere introducir al sistema: "))
impuesto = float(input("Que tasa de impuesto posee(en %): "))

def recibir():

    libros = []

    for libro in range(1, cant_libros + 1):
        libros.append([str(input("Nombre del libro: ")), int(input("Precio del libro: "))])
        print("*"*10)

    return libros

def calcular(libros):

    total = 0
    for libro in libros:
        print("-"*10)
        total += libro[1]
        print("Libro: " + str(libro[0]) + "\tPrecio: " + str(libro[1]))


    impuestos = total * (impuesto / 100)
    print("-"*10)
    print("Precio total: " + str(total))
    print("Impuestos: " + str(impuestos))
    total = total + impuestos
    print("Pagar: "+ str(total))

if __name__=="__main__":
    calcular(recibir())

