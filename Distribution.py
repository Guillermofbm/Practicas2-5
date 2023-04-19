# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:34:49 2023

@author: guill
"""

def ordenamiento_distruns(lista):
    n = len(lista)
    if n <= 1:
        return lista

    # Crear una lista de corridas iniciales
    runs = []
    run = [lista[0]]
    for i in range(1, n):
        if lista[i] >= lista[i-1]: # Si el elemento actual es mayor o igual al elemento anterior, se agrega al run actual
            run.append(lista[i])
        else: # Si el elemento actual es menor que el elemento anterior, se agrega el run actual a la lista de corridas y se comienza un nuevo run
            runs.append(run)
            run = [lista[i]]
    runs.append(run)

    # Realizar la fusión de las corridas
    while len(runs) > 1:
        temp = []
        for i in range(0, len(runs), 2):
            if i == len(runs)-1: # Si solo queda una corrida por fusionar, se agrega a la lista temporal sin fusionar
                temp.append(runs[i])
            else: # Si hay dos corridas por fusionar, se fusionan y se agrega a la lista temporal
                merged_run = merge_runs(runs[i], runs[i+1])
                temp.append(merged_run)
        runs = temp

    return runs[0]

def merge_runs(run1, run2):
    merged_run = []
    i = j = 0
    n1 = len(run1)
    n2 = len(run2)
    while i < n1 and j < n2:
        if run1[i] <= run2[j]: # Si el primer elemento del run 1 es menor o igual que el primer elemento del run 2, se agrega al run fusionado
            merged_run.append(run1[i])
            i += 1
        else: # Si el primer elemento del run 1 es mayor que el primer elemento del run 2, se agrega al run fusionado
            merged_run.append(run2[j])
            j += 1
    if i < n1: # Si quedan elementos en el run 1 después de la fusión, se agregan al run fusionado
        merged_run.extend(run1[i:])
    if j < n2: # Si quedan elementos en el run 2 después de la fusión, se agregan al run fusionado
        merged_run.extend(run2[j:])
    return merged_run

# Ejemplo de uso
lista = [4, 2, 7, 1, 3, 5, 6]
lista_ordenada = ordenamiento_distruns(lista)
print(lista_ordenada)

