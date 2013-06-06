from datetime import datetime
def anoAct():
    #retorna el Ano actual aunque la funcion ya existe
    return datetime.now().year
def personas():
    #recolecta los nombres y el Ano de nacimiento de 3 personas
    i = range(0,3)
    temp = []
    personasList = []
    for a in i:
       nombre = raw_input('Escriba un Nombre: ')
       nacimiento = input('Escriba su ano de nacimiento: ')
       temp = [nombre,nacimiento]
       personasList.append(temp)
    return personasList
def calculaAnos():
    #Calcula los anos e imprime el resultado
    listaPersonas = personas()
    resultadosAnos = []
    anoActual = anoAct()
    cont = 0
    for i in listaPersonas:
       ano = i[1]
       resultadosAnos.append(anoActual-ano)
    for i in listaPersonas:
       nombre = listaPersonas[cont][0]
       nacimiento = listaPersonas[cont][1]
       anos = resultadosAnos[cont]
       cont += 1
       print 'Nombre %s Nacimiento %d Anos a cumplir %d' % (nombre,nacimiento,anos)
    return
calculaAnos()
