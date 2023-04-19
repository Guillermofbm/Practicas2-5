# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 15:23:18 2023

@author: guill
"""
#Creamos una funcion para ordenar listas
def ordenamiento_insercion(lista):
    #Creamos un ciclo con iteraciones del tamaño de la lista
    for i in range(1, len(lista)):
        #Guardamos el numero con el que se esta trabajando
        valor_actual = lista[i]
        #Se crea una variable para trabajar con la posicion
        posicion_actual = i
        #Mientras sigan quedando posiciones que revisar y mientras los valores visitados sean mayores
        #Al numero con el que se esta trabajando
        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            #Recorremos los valores de la derecha hacia la izquierda
            lista[posicion_actual] = lista[posicion_actual - 1]
            #Disminuimos una posicion
            posicion_actual -= 1
            #Asignamos el valor menor a la izquierda
        lista[posicion_actual] = valor_actual

mi_lista = [4, 2, 1, 3, 5]
ordenamiento_insercion(mi_lista)
print(mi_lista)