from typing import Tuple
import networkx as nx
import random as rand
from pprint import pprint
import ast

Point = Tuple[int, int]



class Graph:

    def __init__(self):
        self.nodes = dict()
        self.edges = dict()

    @property
    def size(self):
        return len(self.nodes)

    def add_node(self, node: Point, weight: int):
        self.nodes[node] = weight

        return self
    
    def add_edge(self, node1: Point, node2: Point):
        self.edges.setdefault(node1, []).append(node2) # add edge node1 -> node2

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

            nodes_number = int(line) # number of nodes = number of lines to read

            nodes = dict()
            edges = dict()
            for v in range(1, nodes_number + 1):
                x, y, weight, *neighbours = [int(w) for w in \
                                            file.readline().split()]

                l += 1

                nodes[v] = (x, y)
                self.add_node((x, y), weight) # {node: weight}

                for n in neighbours: # neighbour nodes are nodes 
                                     # that share an edge
                    edges.setdefault(v, []).append(n) 

            break

        for e in edges.keys():
            for n in edges[e]: self.add_edge(nodes[e], nodes[n])

        print(f'nodes: ', self.nodes)
        print(f'edges: ', self.edges)

        return self

    def random_graph(self, size: int, seed: int, edge_probability: int = 0.5):
        self.nodes.clear()
        self.edges.clear()

        rand.seed(seed)

        for _ in range(size):
            while True:
                x, y = (rand.randint(1, 20), rand.randint(1, 20)) # generate
                                                                  # random
                                                                  # coordinates
                if not (x, y) in self.nodes: break # continue if point exists

            self.add_node((x,y), rand.randint(1, 10))
        
        print(f'nodes: ', self.nodes)

        for n1 in self.nodes:
            for n2 in self.nodes:
                if rand.random() < edge_probability and n1 != n2:
                    self.add_edge(n1, n2) # generate edges until given max

        print(f'edges: ', self.edges)
        
        return self

    def draw_graph(self, ax = None):
        graph = nx.DiGraph()

        for key in self.edges.keys():
            for value in self.edges[key]:
                graph.add_edge(key, value)

        pprint(graph.edges)
        
        positions = {x: x for x in graph.nodes}
        
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

    def find_minimum_weighted_closure(self, algorithm: str = "exhaustive"):
        if algorithm == "exhaustive":
            solution = ExhaustiveSearch(self.nodes, self.edges).calculate()
        if algorithm == "greedy":
            solution = GreedySearch(self.nodes, self.edges)

        return solution
                

class ExhaustiveSearch:

    global compute_powerset

    def __init__(self, nodes: dict(), edges: dict()):
        self.nodes = nodes
        self.edges = edges
        self.size = len(nodes)

    def compute_powerset(lst):
        l = len(lst)

        powerset = []
        for i in range(1 << l):
            powerset.append([lst[j] for j in range(l) if (i & (1 << j))])

        return powerset
    
    def calculate(self):
        # a power set of a set S is the set of all subsets of S, 
        # including the empty set and S itself
        powerset = compute_powerset([n for n in self.nodes.keys()])
        
        closures = []
        for possible_closure in powerset:
            print("possible closure: ", possible_closure)

            out_edges = []
            for node in possible_closure:
                print("node: ", node)
                if node in self.edges.keys(): # node has an edge for another node
                    out_edges.extend(x for x in self.edges[node]\
                                    if x not in out_edges)
                    
            print("edges to nodes external to the possible closure: ", out_edges)
            print("")

            if not out_edges and possible_closure: # if no edges leave the 
                                # possible closure and its value != None,
                                # then this subset is a closure
                closures.append(possible_closure)
        
        print("closures: ", closures)

        closures_weights = dict()
        for closure in closures:
            closures_weights[str(closure)] = sum([self.nodes[node] \
                                                for node in closure])

        return ast.literal_eval(min(closures_weights, key = closures_weights.get))
        


class GreedySearch:
    pass