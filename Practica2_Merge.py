# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 21:58:31 2023

@author: guill
"""

#Creamos una funcion de ordenamiento
def merge_sort(array):
    #Si la longitud del arreglo es menor o igual que 1 entonces no se hace nada
    if len(array) <= 1:
        return array
    # Divide el arreglo en dos mitades
    mitad = len(array) // 2
    #Se guarda la primera mitad en un arreglo llamado izquierda
    izquierda = array[mitad:]
    #Se guarda la segunda mitad en un arreglo llamado derecha
    derecha = array[:mitad]
    # Se siguen dividiendo
    izquierda_ordenada = merge_sort(izquierda)
    derecha_ordenada = merge_sort(derecha)
    #Se llama a la funcion merge
    return merge(izquierda_ordenada, derecha_ordenada)
#Se crea una funcion para ordenar los datos
def merge(izquierda, derecha):
    #Se crea una lista vacia y contadores "i" y "j"
    resultado = []
    i = 0
    j = 0
    #Se crea un ciclo para recorrer todos los valores hacia la izquierda y derecha
    while i < len(izquierda) and j < len(derecha):
        #Si el valor de la derecha es mayor que la izquierda 
        if izquierda[i] <= derecha[j]:
            #agregamos el valor de la izquierda
            resultado.append(izquierda[i])
            i += 1
            #Si no
        else:
            #Agregamos el de la derecha
            resultado.append(derecha[j])
            j += 1
    # Agrega los elementos restantes de la mitad izquierda 
    resultado += izquierda[i:]
    # Agrega los elementos restantes de la mitad derecha
    resultado += derecha[j:]
    #devolvemos la lista
    return resultado

arreglo = [3, 5, 1, 4, 2]
arreglo_ordenado = merge_sort(arreglo)
print(arreglo_ordenado)  # [1, 2, 3, 4, 5]
