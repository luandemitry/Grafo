import heapq
import sys

class Graph:
    
    def __init__(self):
        self.vertices = {}
        
    def add_vertice(self, name, edges):
        self.vertices[name] = edges
    
    def caminho_curto(self, start, finish):
        distancia = {} #Distancia do inicio até o nodo
        anterior = {}  
        nodes = [] 

        for vertice in self.vertices:
            if vertice == start: 
                distancia[vertice] = 0
                heapq.heappush(nodes, [0, vertice])
            else:
                distancia[vertice] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertice])
            anterior[vertice] = None
        
        while nodes:
            menor = heapq.heappop(nodes)[1] 
            if menor == finish: 
                path = []
                while anterior[menor]: 
                    path.append(menor)
                    menor = anterior[menor]
                return path
            if distancia[menor] == sys.maxsize: 
                break
            
            for vizinho in self.vertices[menor]: 
                alt = distancia[menor] + self.vertices[menor][vizinho] 
                if alt < distancia[vizinho]: 
                    distancia[vizinho] = alt
                    anterior[vizinho] = menor
                    for n in nodes:
                        if n[1] == vizinho:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)
        return distancia
        
    def __str__(self):
        return str(self.vertices)

if __name__ == '__main__':
    g = Graph()
    g.add_vertice('Barra', {'Pituba': 7, 'Costa azul': 8})
    g.add_vertice('Pituba', {'Barra': 7, 'Amaralina': 2})
    g.add_vertice('Costa azul', {'Barra': 8, 'Amaralina': 6, 'Imbui': 4})
    g.add_vertice('Boca do rio', {'Amaralina': 8})
    g.add_vertice('Ondina', {'Rio Vermelho': 1})
    g.add_vertice('Amaralina', {'Pituba': 2, 'Costa azul': 6, 'Boca do rio': 8, 'Imbui': 9, 'Rio Vermelho': 3})
    g.add_vertice('Imbui', {'Costa azul': 4, 'Amaralina': 9})
    g.add_vertice('Rio Vermelho', {'Ondina': 1, 'Amaralina': 3})
    print(g.caminho_curto('Barra', 'Imbui'))