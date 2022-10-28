from turtle import position
from typing import Tuple
import networkx as nx
from networkx.generators.random_graphs import erdos_renyi_graph

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

    def read_graph(self, filename: str):
        self.vertices.clear()
        self.edges.clear()

        try:
            file = open(filename, "r")
        except FileNotFoundError:
            print(f"Error! File not found!")
            exit(1)

        l = 0
        while file:
            line = file.readline()
            l += 1
            #if not line:
            #    continue

            #vertices_number = len(line.split(" "))
            vertices_number = int(line)
            print(vertices_number)

            vertices = []
            for v in range(vertices_number):
                x, y, weight, *neighbours = [int(w) for w in file.readline().split()]

                l += 1

                vertices.append((x, y))
                self.add_vertice((x, y), weight)

                for n in neighbours:
                    self.add_edge((x, y), vertices[n])
            break

        print(f'Vertices: ', self.vertices)
        print(f'Edges: ', self.edges)

        return self

    def random_graph(self, size: int, seed: int):
        self.vertices.clear()
        self.edges.clear()

        g = erdos_renyi_graph(
            n = size, 
            p = 0.25,
            seed = seed,
            directed = True
        )

        nx.draw_networkx(
            g, 
            pos = nx.spring_layout(g),
            edge_color = 'gray',
            width = 2,
            node_size = 400,
            node_color = '#FFB266',
        )

        print(g.nodes)
        print(g.edges)

        return self

    def draw_graph(self, ax = None):
        graph = nx.Graph()

        for vertices, neighbours in self.edges.items():
            for neighbour in neighbours:
                graph.add_edge(vertices, neighbour)
        
        positions = {x: x for x in graph.nodes} # {node: value}
        
        nx.draw_networkx_edges(
            graph,
            pos = positions,
            nodelist = self.vertices,
            edge_color = 'gray',
            node_size = 200,
            width = 2,
            ax = ax
        )

        nx.draw_networkx_nodes(
            graph,
            pos = positions,
            #labels=sol_vertices,
            nodelist = self.vertices,
            node_size = 400,
            node_color = '#FFB266',
            #node_color=sol_colors,
            #cmap=plot.cm.summer,
            ax = ax
        )

        nx.draw_networkx_labels(
            graph,
            pos = positions,
            labels = self.vertices,
            #font_weight = 'bold',
            font_color = 'black',
            font_size = 8
            #with_labels=True
        )
