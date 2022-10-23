import random as rand
from turtle import position
from typing import Tuple
import networkx as nx
import matplotlib as plot

Point = Tuple[int, int]

class SearchGraph:

    def __init__(self) -> None:
        self.vertices = {}
        self.edges = {}

    @property
    def size(self):
        return len(self.vertices)

    def add_vertice(self, vertice: Point, weight: int):
        self.vertices[vertice] = weight

        return self
    
    def add_edge(self, vertice1: Point, vertice2: Point):
        self.edges.setdefault(vertice1, set()).add(vertice2)
        self.edges.setdefault(vertice2, set()).add(vertice1)

        return self

    def random_graph(self, size: int, seed: int):
        self.vertices.clear()
        self.edges.clear()

        rand.seed(seed)

        vertices = []
        for vertice in range(size):
            while True:
                x, y = (rand.randint(1, 9), rand.randint(1, 9))
                if not (x, y) in self.vertices: break

            vertices.append((x, y))
            self.add_vertice((x, y), rand.randint(1, 99))

        for v1 in range(size - 1):
            for _ in range(rand.randint(1, size // 2)):
                v2 = rand.randint(v1 + 1, size - 1)
                self.add_edge(vertices[v1], vertices[v2])
        
        return self

    def draw_graph(self, ax = None):
        graph = nx.Graph()

        for vertices, neighbours in self.edges.items():
            #print(vertices)
            #print(neighbours)
            for neighbour in neighbours:
                graph.add_edge(vertices, neighbour)
        
        positions = {x: x for x in graph.nodes}
        print(positions)

        #low, *_, high = sorted(self.vertices.values())
        #norm = plot.colors.Normalize(vmin=low, vmax=high, clip=True)
        #mapper = plot.cm.ScalarMappable(norm=norm, cmap=plot.cm.coolwarm)
        #colors = [mapper.to_rgba(i) for i in self.vertices.values()]
        
        nx.draw_networkx_edges(
            graph,
            pos=positions,
            nodelist=self.vertices,
            edge_color='gray',
            node_size=200,
            width=2,
            ax=ax
        )

        nx.draw_networkx_nodes(
            graph,
            pos=positions,
            #labels=sol_vertices,
            nodelist=self.vertices,
            node_size=200,
            #node_color=sol_colors,
            #cmap=plot.cm.summer,
            ax=ax
        )

        #nx.draw_networkx_labels(
        #    graph,
        #    pos=positions,
        #    labels=self.vertices,
        #    font_weight='bold',
        #    font_color='black',
        #    #with_labels=True
        #)
