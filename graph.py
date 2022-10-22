import random as rand
from typing import Tuple
import networkx as nx
import matplotlib as plot

Point = Tuple[int, int]

class SearchGraph:

    def __init__(self) -> None:
        self.vertices = {}
        self.edges = {}

    def add_vertice(self, vertice: Point, weight: int):
        self.vertices[vertice] = weight

        return self
    
    def add_edge(self, vertice1: Point, vertice2: Point):
        self.edges.setdefault(vertice1, set()).add(vertice2)
        self.edges.setdefault(vertice2, set()).add(vertice1)

        return self

    def random_graph(self, size: int, seed: int = 93107):
        self.vertices.clear()
        self.edges.clear()

        rand.seed(seed)

        for vertice in range(size):
            while True:
                x, y = (rand.randint(1, 9), rand.randint(1, 9))
                if not (x, y) in self.vertices: break

            self.vertices.append((x, y))
            self.add_vertice((x, y), rand.randint(1, 99))

        for v1 in range(size - 1):
            for _ in range(rand.randint(1, size // 2)):
                v2 = rand.randint(v1 + 1, size - 1)
                self.add_edge(self.vertices[v1], self.vertices[v2])
        
        return self