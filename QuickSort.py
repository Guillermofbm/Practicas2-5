# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 21:44:34 2023

@author: guill
"""
#Creamos una funcion de ordenamiento rapido
def quicksort(array):
    #si la longitud del arreglo es menor que 2
    if len(array) < 2:
        #no se hace nada con la lista
        return array
    else:
        #Se guarda el primer valor
        pivote = array[0]
        #se guardaran en una lista aquellos valores que sean menores al primer elemento
        menores = [x for x in array[1:] if x <= pivote]
        #se guardaran en una lista aquellos valores que sean mayores al primer elemento
        mayores = [x for x in array[1:] if x > pivote]
        #rellamaremos esta misma fuincion hasta que las listas tengan menos que 2 elementos y se devuelve la lista final
        return quicksort(menores) + [pivote] + quicksort(mayores)

datos = [2, 5, 8, 1, 4, 9, 3]
datos_ordenados = quicksort(datos)
print(datos_ordenados)