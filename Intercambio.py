# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 21:12:24 2023

@author: guill
"""

#Creamos una funcion para ordenar listas
def ordenamiento_intercambio(lista):
    #Creamos un ciclo que haga el 1 iteracion menos que la longitud de la lista
    for i in range(len(lista)-1):
        #Creamos un ciclo que haga el numero de iteraciones que de longitud de la lista
        #Pero empezando desde la posicion siguiente
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                # Intercambiar elementos
                lista[i], lista[j] = lista[j], lista[i]
    return lista
mi_lista = [4, 2, 7, 1, 3, 5, 6]
print(ordenamiento_intercambio(mi_lista))
