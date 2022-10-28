from typing import Tuple
import networkx as nx
import random as rand
from pprint import pprint

Point = Tuple[int, int]

class Graph:

    def __init__(self) -> None:
        self.nodes = {}
        self.edges = {}

    @property
    def size(self):
        return len(self.nodes)

    def add_node(self, node: Point, weight: int):
        self.nodes[node] = weight

        return self
    
    def add_edge(self, node1: Point, node2: Point):
        self.edges.setdefault(node1, []).append(node2)

        return self

    def read_graph(self, filename: str):
        self.nodes.clear()
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

            nodes_number = int(line)
            print(nodes_number)

            nodes = dict()
            edges = dict()
            for v in range(1, nodes_number + 1):
                x, y, weight, *neighbours = [int(w) for w in file.readline().split()]

                l += 1

                nodes[v] = (x, y)
                self.add_node((x, y), weight)

                for n in neighbours:
                    edges.setdefault(v, []).append(n)

                #for n in neighbours:
                #    self.add_edge((x, y), nodes[n])

            break
        
        print("nodes: ", nodes)
        print("edges: ", edges)

        for e in edges.keys():
            for n in edges[e]:
                self.add_edge(nodes[e], nodes[n])

        print("\n")
        print("\n")
        print(f'nodes: ', self.nodes)
        print(f'edges: ', self.edges)

        return self

    def random_graph(self, size: int, seed: int, edge_probability: int = 0.5):
        assert 2 <= size <= 81, "Size must be between [2, 81]"

        self.nodes.clear()
        self.edges.clear()
        rand.seed(seed)

        for _ in range(1, size):
            while True:
                x, y = (rand.randint(1, 20), rand.randint(1, 20))
                if not (x, y) in self.nodes: break

            self.add_node((x,y), rand.randint(1, 10))
        
        print(self.nodes)

        all_nodes_combinations = [(n1, n2) for n1 in self.nodes for n2 in self.nodes if n1 != n2]

        #pprint(all_nodes_combinations)

        for n1 in self.nodes:
            for n2 in self.nodes:
                if rand.random() < edge_probability and n1 != n2:
                    self.add_edge(n1, n2)

        print(self.edges)
        
        return self

    def draw_graph(self, ax = None):
        graph = nx.DiGraph()

        for key in self.edges.keys():
            for value in self.edges[key]:
                graph.add_edge(key, value)

        pprint(graph.edges)
        
        positions = {x: x for x in graph.nodes} # {node: value}
        
        nx.draw(
            graph,
            pos = positions,
            nodelist = self.nodes,
            edge_color = 'gray',
            node_size = 400,
            node_color = '#FFB266',
            width = 2,
            ax = ax,
            arrows = True,
            arrowsize = 10,
            arrowstyle='->'
        )

        nx.draw_networkx_labels(
            graph,
            pos = positions,
            labels = self.nodes,
            font_color = 'black',
            font_size = 8
        )

