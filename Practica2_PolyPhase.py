# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:44:25 2023

@author: guill
"""

def ordenamiento_polyphase(lista):
    # Si la longitud de la lista es 1 o menos, ya está ordenada
    n = len(lista)
    if n <= 1:
        return lista
    
    # Dividir la lista en dos sublistas
    mitad = n // 2     # Obtener el índice de la mitad de la lista
    izquierda = lista[:mitad]   # Crear la sublista izquierda desde el inicio hasta la mitad de la lista original
    derecha = lista[mitad:]     # Crear la sublista derecha desde la mitad hasta el final de la lista original
    
    # Ordenar las sublistas de forma recursiva
    izquierda_ordenada = ordenamiento_polyphase(izquierda)   # Llamada recursiva para ordenar la sublista izquierda
    derecha_ordenada = ordenamiento_polyphase(derecha)       # Llamada recursiva para ordenar la sublista derecha
    
    # Combinar las sublistas en una sola lista ordenada
    lista_ordenada = []
    while len(izquierda_ordenada) > 0 and len(derecha_ordenada) > 0:
        if izquierda_ordenada[0] <= derecha_ordenada[0]:
            # El primer elemento de la lista izquierda es menor o igual al primer elemento de la lista derecha, por lo que se agrega a la lista ordenada
            lista_ordenada.append(izquierda_ordenada.pop(0))
        else:
            # El primer elemento de la lista derecha es menor que el primer elemento de la lista izquierda, por lo que se agrega a la lista ordenada
            lista_ordenada.append(derecha_ordenada.pop(0))
    
    # Agregar los elementos restantes de las listas izquierda y derecha a la lista ordenada
    lista_ordenada += izquierda_ordenada
    lista_ordenada += derecha_ordenada
    
    return lista_ordenada

# Ejemplo de uso
lista = [4, 2, 7, 1, 3, 5, 6]
lista_ordenada = ordenamiento_polyphase(lista)
print(lista_ordenada)
