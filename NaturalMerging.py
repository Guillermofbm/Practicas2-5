# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:17:20 2023

@author: guill
"""

# creamos una funcion de ordenamiento
def ordenamiento_natural_merge(lista):
    #creamos una lista
    subsecuencias = []
    #creamos una memoria
    inicio_subsecuencia = 0
    #creamos un ciclo para recorrer toda la longitud de la lista
    for i in range(1, len(lista)):
        #si el numero actual es menor al siguiente 
        if lista[i] < lista[i-1]:
            #agregamos a la lista los valores que se encuentren hasta i
            subsecuencias.append(lista[inicio_subsecuencia:i])
            #actualizamos el valor de la secuencia
            inicio_subsecuencia = i
    #Al final del ciclo se agregan los valores que faltaron
    subsecuencias.append(lista[inicio_subsecuencia:])

    # Creamos un ciclo hasta que la longitud de la lista sea menor o igual que 1
    while len(subsecuencias) > 1:
        #creamos una lista
        resultado = []
        #creamos un ciclo para recorrer la lista de 2 en 2
        for i in range(0, len(subsecuencias), 2):
            #si i es igual a la longitud de la secuencia menos 1
            if i == len(subsecuencias) - 1:
                #agregamos el valor siguiente a la lista del resultado
                resultado.append(subsecuencias[i])
                #si no
            else:
                #Se agregan los valores que devuelva la funcion 
                resultado.append(combinar_subsecuencias(subsecuencias[i], subsecuencias[i+1]))
        subsecuencias = resultado

    return subsecuencias[0]

#Creamos una funcion para mezclar las secuencias
def combinar_subsecuencias(subsecuencia1, subsecuencia2):
    #creamos una lista
    combinado = []
    #creamos 2 contadores
    i = j = 0
    #creamos un ciclo para recorrer las listas
    while i < len(subsecuencia1) and j < len(subsecuencia2):
        #si la secuencia 1 es menor que la 2
        if subsecuencia1[i] < subsecuencia2[j]:
            #se agrega la secuencia 1 a la lista
            combinado.append(subsecuencia1[i])
            i += 1
            #si no
        else:
            #se agrega la 2
            combinado.append(subsecuencia2[j])
            j += 1
    combinado.extend(subsecuencia1[i:])
    combinado.extend(subsecuencia2[j:])
    return combinado

arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(ordenamiento_natural_merge(arr))