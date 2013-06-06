#Grupo de estudio de Python G+.

#Unidad 2 - Desafio 1

"""Escribir un programa que convierta de numeros decimales a binarios y viceversa."""

#Carlos Llamacho

def binario(decimal):
	
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
def decimal(binario):
    
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


if __name__=="__main__":
	binario = int(input("Introduce un numero binario: "))
	
	print(decimal(binario))
