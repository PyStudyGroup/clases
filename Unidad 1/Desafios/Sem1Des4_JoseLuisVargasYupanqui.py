#Unidad 1 Desafio 4
#Desarrollado por Jose Vargas

#triangulo superior 
def jose(n):
	cad=""
	cad1=""
	cad2=""
	for i in range(n):
		cad1=cad1+str(i+1)#primer cuadrante
		vac=" "
		x=n-i
		for j in range(x):
			cad=cad+vac #genera los vacios para el primer cuadrante
		for w in range(i):
			cad2=cad2+str(i-w)#segundo cuadrante
		cad=cad+cad1+cad2
		print cad
		cad=""
		cad2=""

#triangulo inferior 		
def jose1(n):
	cad1=""
	cad2=""
	vac=" "
	for i in range(n-1):
		vac=vac*(i+2) #genera los vacios para el tercer cuadrante
		for j in range(n-i-1):
			cad2=cad2+str(j+1)#tercer cuadrante
		for k in range(n-i-2):
			cad1=cad1+str(n-i-k-2)#cuarto cuadrante
		print vac+cad2+cad1
		cad1=""
		cad2=""
		vac=" "
def main():
	n=input("Ingrese un numero: ")
	jose(n)
	jose1(n)
main()