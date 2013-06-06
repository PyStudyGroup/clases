#Grupo de estudio de Python G+.

#Unidad 2 - Desafio 1

"""Escribir un programa que convierta de numeros decimales a binarios y viceversa."""

#Carlos Llamacho

from sys import exit

def conv_binario(decimal):
	
	resultado = ""
	
	#Loop para el algoritmo.
	while decimal != 0:
		#Resto del numero a convertir, este es el numero binario.
		resultado += str(decimal % 2)
		#Esto reduce el numero decimal hasta que se convierte en 0.
		decimal = decimal // 2

        resultado = virar(resultado)
	return resultado

#Funcion que convierte de binario a decimal.
def conv_decimal(binario):
    
    #Para fines de conversion virar el binario.
    binario = virar(binario)

    #Convertirlo en string para fines de iteracion
    binario = str(binario)

    #Variables para usar en proceso.
    decimal = 0
    tam = range(len(binario))
    counter = len(binario)

    #Loop principal.
    for num in binario:
        decimal += int(num) * (2**tam[-counter])
        counter -= 1

    #Numero decimal.
    return decimal

#Funcion que coge un numero binario y lo vira al reves.
def virar(binario):

    #Convertirlo a string para fines de iteracion.
    binario = str(binario)
    tam = len(binario) - 1
    binario_reves = ""

    #Loop principal.
    for num in binario:
        binario_reves += binario[tam]     
        tam -= 1

    return binario_reves


def main():
    """Funcion que nos muestra un menu para seleccionar que querremos convertir."""

    print("Opciones: ")
    print("-"*25)
    print("1- De binario a decimal.")
    print("2- De decimal a binario.")
    print("3- Salir.\n")

    opcion = int(input("Elija su opcion (1,2,3): "))
    
    while True:
        if opcion in range(1, 4):
            break
        else:
            opcion = int(input("Incorrecto, elija nuevamente: "))
    
    if opcion == 3:
        exit()
    elif opcion == 1:
        binario = input("Introduce un # binario: ")
        print("-"*25)
        print("El numero binario {0} da el numero decimal {1}.".format(binario, conv_decimal(binario)))
        print("-"*25)
        main()
    elif opcion == 2:
        decimal = input("Introduce un # decimal: ")
        print("-"*25)
        print("El numero decimal {0} da el numero binario {1}.".format(decimal, conv_binario(decimal)))
        print("-"*25)
        main()
    
main()