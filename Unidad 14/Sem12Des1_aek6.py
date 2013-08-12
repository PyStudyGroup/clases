#! /usr/bin/python
# -*- coding: utf-8 -*-
from os import system
from time import sleep
import random

cuadro = 'O'
#============================== Figura ====================================
class Figura():
    
    def __init__(self, forma):
        if forma == 'T':
            self.forma = [[' ',cuadro,' '],[cuadro,cuadro,' '],[' ',cuadro,' ']]
        elif forma == 'Z':
            self.forma = [[cuadro,' ',' '],[cuadro,cuadro,' '],[' ',cuadro,' ']]
        elif forma == '|':
            self.forma = [[cuadro,' ',' ',' '],[cuadro,' ',' ',' '],[cuadro,' ',' ',' '],[cuadro,' ',' ',' ']]
        elif forma == 'L':
            self.forma = [[cuadro,' ',' '],[cuadro,' ',' '],[cuadro,cuadro,' ']]
        elif forma == 'iZ':
            self.forma = [[' ',cuadro,' '],[cuadro,cuadro,' '],[cuadro,' ',' ']]
        else:
            self.forma = [[cuadro,cuadro],[cuadro,cuadro]]
        #self.forma = [[' ','O','O'],['O','O','O'],['O',' ',' ']]
    
    def cambia(self):
        temp = []
        i = 0
        for fila in self.forma:
            temp.append([])
            for columna in fila:
                temp[i].append(columna)
            i += 1
        
        cc = -1
        for f in temp:
            ff = len(temp) - 1
            cc += 1
            for c in f:
                self.forma[ff][cc] = c
                ff -= 1
        return temp
        
        
#============================ Contenedor ================================
class Contenedor():
    
    def __init__(self, filas, columnas):
        self.contenedor = []
        for f in range(0, filas):
            self.contenedor.append([])
            for c in range(0, columnas):
                if f == 0 or f == filas-1 or c == 0 or c == columnas-1:
                    self.contenedor[f].append('/')
                    continue
                self.contenedor[f].append(' ')
        
    
    def dibujar(self):        
        system('clear')
        for x in range(0, len(self.contenedor)):
            text = ''
            for y in range(0, len(self.contenedor[x])):
                text += str(self.contenedor[x][y])
            print(text)
            
    def agregar(self, obj, x, y):
        temp = y
        for f in obj.forma:
            for c in f:
                if c != ' ':
                    #not (x == 0 or x == len(self.contenedor)-1 or y == 0 or y == len(self.contenedor[x])):
                    self.contenedor[x][y] = c
                y += 1
            y = temp
            x += 1
            
    def disponible(self, obj, x, y):
        validados = []
        #x += len(obj.forma)-1
        for fi in range(len(obj.forma)-1, -1, -1):
            for ci in range(len(obj.forma)-1, -1, -1):
                print(fi,ci)
                if obj.forma[fi][ci] != ' ':
                    if ci not in validados:
                        if self.contenedor[x+fi][y+ci] != ' ':
                            return False
                        else:
                            validados.append(ci)
        return True
        
#====================================================================        
contenedor = Contenedor(20,20)

for i in range(30):
    forma = ('T','Z','L','|','iZ','#')
    f1 = Figura(forma[random.randrange(0,6)])
    x = 1
    y = random.randrange(1,17)
    while(True):
        contenedor.agregar(f1, x, y)
        contenedor.dibujar()
        sleep(0.2)
            
        #avanzar abajo
        if not contenedor.disponible(f1, x+1, y):
            break
        
        #limpiar
        for fi in range(len(f1.forma)):
            for ci in range(len(f1.forma)):
                if f1.forma[fi][ci] == cuadro:
                    contenedor.contenedor[x+fi][y+ci] = ' '
        x += 1
        
        #rotar
        tempforma = f1.cambia()
        if not contenedor.disponible(f1, x, y):
            f1.forma = tempforma
        
        