# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:21:50 2023

@author: guill
"""

#Creamos una funcion de ordenamiento el parametro k dividira la lista en n elementos por lista
def balanced_multiway_merge_sort(lista, k):
    #Dividimos las listas en varias del mismo tamaño
    sub_listas = [lista[i:i+k] for i in range(0, len(lista), k)]

    # creamos un cilco para entrar en todos los elementos de las sublistas
    for i in range(len(sub_listas)):
        #agregamos el valor que nos devulve la funcion
        sub_listas[i] = merge_sort(sub_listas[i])

    # Creamos una lista
    resultado = []
    indices_sublistas = [0] * len(sub_listas)
    
    #creamos un ciclo hasta que se cierre manualmente
    while True:
        #creamos 2 varibles
        min_valor = float('inf')
        min_indice_sublista = -1

        #creamos un ciclo para todos los elementos de las listas
        for i in range(len(sub_listas)):
            #si el indice es menor que la longitud de la lista
            if indices_sublistas[i] < len(sub_listas[i]):
                if sub_listas[i][indices_sublistas[i]] < min_valor:
                    #se guarda el valor de la sublista
                    min_valor = sub_listas[i][indices_sublistas[i]]
                    #Se actualiza el indice
                    min_indice_sublista = i

        # Si no hay más valores, termina el ciclo
        if min_indice_sublista == -1:
            break

        # Agrega el valor a la lista ordenada y mueve el índice de la sub-lista correspondiente
        resultado.append(min_valor)
        indices_sublistas[min_indice_sublista] += 1

    return resultado

#creamos una funcion para unir listas
def merge_sort(lista):
    # Si la lista es de longitud 1 o 0, ya está ordenada
    if len(lista) <= 1:
        return lista

    # Divide la lista en dos mitades y ordena cada mitad por separado utilizando el algoritmo merge sort
    medio = len(lista) // 2
    mitad_izquierda = merge_sort(lista[:medio])
    mitad_derecha = merge_sort(lista[medio:])

    # Combina las dos mitades ordenadas en una sola lista ordenada
    resultado = []
    i = j = 0

    while i < len(mitad_izquierda) and j < len(mitad_derecha):
        if mitad_izquierda[i] < mitad_derecha[j]:
            resultado.append(mitad_izquierda[i])
            i += 1
        else:
            resultado.append(mitad_derecha[j])
            j += 1

    resultado += mitad_izquierda[i:]
    resultado += mitad_derecha[j:]

    return resultado

mi_lista = [4, 2, 7, 1, 3, 5, 6]
print(balanced_multiway_merge_sort(mi_lista,2))