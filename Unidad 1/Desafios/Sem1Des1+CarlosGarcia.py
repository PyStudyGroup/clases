fecha_actual = int(raw_input("Ingrese el anio actual: "))
print ""
nombre = []
fecha = []
i = 1
n=0

while i <= 3:
	nombre.append(raw_input('Ingrese su nombre: '))
	fecha.append(int(raw_input('Ingrese su anio de nacimiento: ')))
	print ""
	i = i+1

for item in fecha:
	edad_actual = fecha_actual - item
	print "-"*30
	print "%s tu edad actual es %d" %(nombre[n], edad_actual)
	print "-"*30
	n = n+1
	

raw_input()


