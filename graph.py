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

    def draw_graph(self, ax = None):
        graph = nx.Graph()

        for vertices, neighbours in self.edges.items():
            for neighbour in neighbours:
                graph.add_edge(vertices, neighbour)
        
        positions = {x: x for x in graph.nodes}

        low, *_, high = sorted(self.vertices.values())
        norm = plot.colors.Normalize(vmin=low, vmax=high, clip=True)
        mapper = plot.cm.ScalarMappable(norm=norm, cmap=plot.cm.coolwarm)
        colors = [mapper.to_rgba(i) for i in self.vertices.values()]

        sol_vertices = {}
        sol_colors = []
        rem_vertices = {}
        rem_colors = []

        for i, (v, w) in enumerate(self.vertices.items()):
            if v in self.solution[1][0]:
                sol_vertices[v] = w
                sol_colors.append(colors[i])

            else:
                rem_vertices[v] = w
                rem_colors.append(colors[i])
        
        nx.draw_networkx_edges(
            graph,
            pos=positions,
            nodelist=self.vertices,
            edge_color='gray',
            node_size=500,
            width=2,
            ax=ax)

        nx.draw_networkx_nodes(
            graph,
            pos=positions,
            labels=sol_vertices,
            nodelist=sol_vertices,
            node_size=800,
            node_color=sol_colors,
            cmap=plot.cm.summer,
            ax=ax)

        rem_nodes = nx.draw_networkx_nodes(
            graph,
            pos=positions,
            labels=rem_vertices,
            nodelist=rem_vertices,
            node_size=500,
            node_color='white',
            cmap=plot.cm.summer,
            ax=ax)
        rem_nodes.set_edgecolors(rem_colors)
        rem_nodes.set_linewidth(2)

        nx.draw_networkx_labels(
            graph,
            pos=positions,
            labels=self.vertices,
            font_weight='bold',
            font_color='black',
            with_labels=True)
