#!coding: utf-8
import time, os, sys

# Obtenemos año actual
Anno = time.localtime().tm_year
# Inicializamos personas
Personas = {}

# Obtenemos los datos
for i in range(1,4) :
    Nombre = raw_input("Indique Nombre: ")
    AnnoN = raw_input("Indique Ano de nacimiento: ")
    Personas[Nombre] = AnnoN

# Limpiamos pantalla
if  sys.platform == "linux2":
    os.system('clear')
else:
    os.system("cls")

# Mostramos edad
for i in Personas:
    print "%s cumplirá %d años." %(i, Anno - int(Personas[i]))
