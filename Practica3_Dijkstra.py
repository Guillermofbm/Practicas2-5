# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 23:34:26 2023

@author: guill
"""

import heapq
import math
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph, start, end):
    distancias = {nodo: math.inf for nodo in graph}
    distancias[start] = 0
    cola_prioridad = [(0, start)]
    anteriores = {nodo: None for nodo in graph}

    while cola_prioridad:
        (dist_actual, nodo_actual) = heapq.heappop(cola_prioridad)

        if nodo_actual == end:
            # Ya encontramos la ruta más corta hasta el nodo final, podemos terminar la búsqueda
            break

        if dist_actual > distancias[nodo_actual]:
            continue

        for nodo_vecino, peso_arista in graph[nodo_actual].items():
            nueva_distancia = distancias[nodo_actual] + peso_arista

            if nueva_distancia < distancias[nodo_vecino]:
                distancias[nodo_vecino] = nueva_distancia
                anteriores[nodo_vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (nueva_distancia, nodo_vecino))

    # Construimos la ruta más corta a partir de los nodos anteriores
    ruta = []
    nodo_actual = end
    while nodo_actual is not None:
        ruta.append(nodo_actual)
        nodo_actual = anteriores[nodo_actual]
    ruta.reverse()

    return distancias[end], ruta


def dibujar_grafo(graph):
    G = nx.Graph(graph)
    nx.draw(G, with_labels=True)
    plt.show()


# Ejemplo de uso
n = int(input("Ingrese la cantidad de nodos: "))
graph = {}
for i in range(n):
    graph[i] = {}
for i in range(n):
    for j in range(i + 1, n):
        respuesta = input(f"Hay conexión entre el nodo {i} y el nodo {j}? (si/no): ")
        if respuesta.lower() == "si":
            costo = int(input(f"Ingrese el costo entre el nodo {i} y el nodo {j}: "))
            graph[i][j] = costo
            graph[j][i] = costo
        elif respuesta.lower() == "no":
            graph[i][j] = math.inf
            graph[j][i] = math.inf
        else:
            print("Por favor ingrese una respuesta válida (si/no).")
            exit()
start = int(input("Ingrese el nodo inicial: "))
end = int(input("Ingrese el nodo final: "))
distancia, ruta = dijkstra(graph, start, end)
print("La distancia más corta es:", distancia)
print("La ruta más corta es:", ruta)

dibujar_grafo(graph)

