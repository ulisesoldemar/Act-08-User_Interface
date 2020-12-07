import math
from collections import deque

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    return math.sqrt(((x_2-x_1)**2) + ((y_2-y_1)**2))

def busqueda_profundidad(grafo:dict, origen):
    pila = deque([origen])
    visitados = set([origen])
    ruta = []
    print("Origen:", origen)
    print("Profundidad")
    while pila:
        vertice = pila.popleft()
        print(vertice)
        ruta.append(str(vertice))
        for ady in grafo[vertice]:
            if ady[0] not in visitados:
                visitados.add(ady[0])
                pila.appendleft(ady[0])
    return '\n'.join(ruta)

def busqueda_amplitud(grafo:dict, origen):
    cola = deque([origen])
    visitados = set([origen])
    ruta = []
    print("Origen:", origen)
    print("Amplitud")
    while cola:
        vertice = cola.popleft()
        print(vertice)
        ruta.append(str(vertice))
        for ady in grafo[vertice]:
            if ady[0] not in visitados:
                visitados.add(ady[0])
                cola.append(ady[0])
    return '\n'.join(ruta)
                
