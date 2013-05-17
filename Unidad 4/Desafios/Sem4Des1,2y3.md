Sem4Des1+Nombre
=============

**Propuesta:** 
>Una funcion que reciba un array (de lo que sea) y devuelva un array sin repeticiones.

**Ejemplos:**

	>>>unicos([])
	[]

	>>>unicos([1,3,1,3])
	[1,3]

	>>>unicos([1,3,5,6,6,5,3,1,9711])
	[1,3,5,6,9711]


**Dificultad:** media


Sem4Des2+Nombre
=============

**Propuesta:** 
>Dada una lista de strings, la funcion devuelve el contador del numero de strings donde la longitud del string es 2 o mayor y el primer y el ultimo caracter del string son iguales.

**Ejemplo:**
	
	>>>funcion(["","x","xy","xyx","xx"])
	2


**Dificultad:** media-alta


Sem4Des3+Nombre
=============

**Propuesta:**
>Dada una lista de strings, devuelve la lista con los strings ordenados, excepto los que empiezan con "x", que van al principio.

**Ejemplo:**

	>>>ordenarX(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
	['xanadu', 'xyz', 'aardvark', 'apple', 'mix']

>[[Nota: la funcion sorted(lista) devuelve la lista ordenada, y sorted(lista, reverse=True) la devuelve ordenada inversa.]]

**Dificultad:** alta
