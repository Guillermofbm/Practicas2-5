# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 15:58:20 2023

@author: guill
"""

#Creamos una funcion para ordenar listas
def ordenamiento_seleccion(lista):
    #Creamos un ciclo con iteraciones del tamaño de la lista
    for i in range(len(lista)):
        #Guardamos en una variable la posicion en la que vamos
        indice_minimo = i
        #iniciamos un ciclo que inicie en la posicion inmediata siguiente 
        for j in range(i+1, len(lista)):
            #Si el numero en la posicion j es mayor que el actual 
            if lista[j] < lista[indice_minimo]:
                #se guarda el indice
                indice_minimo = j
        #se intercambian el numero menor con el actual
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
mi_lista = [4, 2, 1, 3, 5]
ordenamiento_seleccion(mi_lista)
print(mi_lista)