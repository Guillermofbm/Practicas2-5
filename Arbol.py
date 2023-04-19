# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 21:25:40 2023

@author: guill
"""
#Creamos una clase  con elementos "valor","izq","der", y parametro "valor" todos inicializados en cero menos el paramatro
class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
#Creamos una funcion que agregue un nodo al arbol
def agregar_nodo_arbol(raiz, valor):
    #Si la raiz esta vacia entonces se le asigna el valor del nodo
    if raiz is None:
        raiz = NodoArbol(valor)
        #si no esta vacia y el valor del nodo es menor al valor de la raiz agregamos el valor a la derecha
    elif valor < raiz.valor:
        raiz.izq = agregar_nodo_arbol(raiz.izq, valor)
        #si no agregamos el valor a la derecha
    else:
        raiz.der = agregar_nodo_arbol(raiz.der, valor)
    return raiz
#Creamos una funcion para mostrar la lista ordenada
def recorrido_en_orden(raiz):
    #si hay raiz
    if raiz:
        #Se llama la misma funcion hasta que siga habiuendo raizes
        recorrido_en_orden(raiz.izq)
        #se imprime el valor 
        print(raiz.valor, end=' ')
        recorrido_en_orden(raiz.der)

mi_arbol = None
valores = [5, 3, 7, 2, 4, 6, 1]
for valor in valores:
    mi_arbol = agregar_nodo_arbol(mi_arbol, valor)
recorrido_en_orden(mi_arbol)

