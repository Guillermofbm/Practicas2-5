# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:03:16 2023

@author: guill
"""
#Creamos una funcion para ordenamiento
def straight_merging_sort(arr):
    # Divide el arreglo en elementos individuales
    sublistas = [[x] for x in arr]
    # creamos un ciclo para recorrer la longitud de las listas
    while len(sublistas) > 1:
        #creamos una lista
        nueva_lista = []
        # Creamos un ciclo que recorra la longitud de las listas con pasos de 2
        for i in range(0, len(sublistas), 2):
            #si la longitud es mayor que el ciclo+1
            if i+1 < len(sublistas):
                #Guardamos los siguientes 2 datos
                l1 = sublistas[i]
                l2 = sublistas[i+1]
                
                nueva_sublista = []
                #mienmtras que la longitud de el numero actual y siguiente sea mayor que 0 
                while len(l1) > 0 and len(l2) > 0:
                    #si el numero siguiente es mayor que el actual entonces se saca el numero actual
                    if l1[0] < l2[0]:
                        nueva_sublista.append(l1.pop(0))
                        #viceversa
                    else:
                        nueva_sublista.append(l2.pop(0))
                #aumentamos en 1 el valor actual y el siguiente
                nueva_sublista += l1
                nueva_sublista += l2
                
                nueva_lista.append(nueva_sublista)
            else:
                # Si hay una sublista impar, la agrega sin combinar
                nueva_lista.append(sublistas[i])
        sublistas = nueva_lista
    
    # Devuelve el arreglo ordenado
    return sublistas[0]
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(straight_merging_sort(arr))