# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 22:19:11 2023

@author: guill
"""
#Creamos un funcion para ordenar datos
def ordenamiento_radix(arr):
    # Encuentra el número máximo
    max_num = max(arr)
    exp = 1
    
    #Creamos mientras el numero mayor entre el numero del exponente sea mayor que 0
    while max_num // exp > 0:
        # Creamos un arreglo de contadores
        contador = [0] * 10
        # Ciclamos entre todos. los numeros del arreglo
        for i in arr:
            #Cada numero se divide entre el exponente y entre 10 y guarda el residuo
            digito = (i // exp) % 10
            #se le agrega 1 al valor del arreglo en la posicion digito
            contador[digito] += 1
        #Creamos un ciclo de 1 a 10
        for i in range(1, 10):
            #sumamos los valores de la izquierda a los de la derecha
            contador[i] += contador[i-1]
        resultado = [0] * len(arr)
        #recorremos el arreglo de derecha a izquierda
        for i in reversed(arr):
            #hacemos nuevamente el paso de la linea 20
            digito = (i // exp) % 10
            #restamos 1 al valor del arreglo en la posicion del digito
            index = contador[digito] - 1
            #asignamos el valor de la iteracion el arreglo del resultado
            resultado[index] = i
            #restamos 1 al valor del contrador en la posicion del arreglo
            contador[digito] -= 1
        
        # creamos un ciclo para todos los valores
        for i in range(len(arr)):
            #asignamos el valor del resultado en la lista
            arr[i] = resultado[i]
        
        # Incrementa el exponente para la siguiente iteración
        exp *= 10
    
    # Devuelve el arreglo ordenado
    return arr
arr = [170, 45, 75, 90, 802, 24, 2, 66]
ordenamiento_radix(arr)
print(arr)
