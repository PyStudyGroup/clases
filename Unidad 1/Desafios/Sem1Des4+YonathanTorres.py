ANCHO_DE_LINEA = 80


def generar_linea(n):
    numeros = range(1, n + 1)
    numeros.extend(numeros[::-1][1:])
    espacios = (ANCHO_DE_LINEA - len(numeros)) / 2
    tmp = ''
    for elem in numeros:
        tmp += str(elem)
    linea = '{0}{1}{0}'.format(' ' * espacios, tmp)
    return linea


nro = int(raw_input('Ingresa un numero: '))

nros = range(1, nro + 1)
nros.extend(nros[::-1][1:])

for i in nros:
    print generar_linea(i)
