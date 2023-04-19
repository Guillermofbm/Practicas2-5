# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 22:51:13 2023

@author: guill
"""

import heapq
import math
import networkx as nx
import matplotlib.pyplot as plt

def prim(graph, start):
    visited = set([start])
    edges = [
        (cost, start, to)
        for to, cost in graph[start].items()
    ]
    heapq.heapify(edges)
    mst_cost = 0
    mst_edges = []
    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst_cost += cost
            mst_edges.append((frm, to, cost))
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))
    return mst_cost, mst_edges

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
mst_cost, mst_edges = prim(graph, start)
print("El costo del árbol parcial mínimo es:", mst_cost)
print("Las aristas del árbol parcial mínimo son:")
for frm, to, cost in mst_edges:
    print(f"({frm}, {to}): {cost}")

# Visualización del grafo
G = nx.Graph(graph)
edge_labels = nx.get_edge_attributes(G, 'weight')
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
nx.draw_networkx_labels(G, pos, font_size=15, font_family='sans-serif')
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
plt.show()




