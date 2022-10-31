import argparse
import matplotlib.pyplot as plot
from graph import Graph

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = 'Find a Minimum Weighted Closure for a Given Vertex-Weighted Directed Graph'
    )
    parser.add_argument(
        '-f',
        '--file',
        metavar = 'FILE', 
        type = argparse.FileType('r'),
        help = 'Load a graph from a given file'
    )
    parser.add_argument(
        '-r',
        '--random',
        metavar = 'SEED',
        type = int,
        help = 'Create a random graph given a seed'
    )
    parser.add_argument(
        '-v',
        '--vertices', 
        metavar = 'N', 
        default = 15, 
        type = int, 
        required = False,
        help = 'number of vertices of the graph (default: %(default)s)'
    )
    parser.add_argument(
        '-e',
        '--edges', 
        metavar = 'N', 
        default = 0.25, 
        type = float, 
        required = False,
        help = 'maximum number of edges (default: %(default)s)'
    )
    parser.add_argument(
        '-a', 
        '--algorithm', 
        metavar = 'NAME', 
        default = 'exhaustive', 
        type = str, 
        required = False,
        choices = ['exhaustive', 'greedy'],
        help = 'number of vertices of the graph (default: %(default)s)'
    )
    parser.add_argument(
        '-d', 
        '--draw', 
        action = 'store_true',
        required = False,
        help = 'draw graph'
    )

    args = vars(parser.parse_args())

    seed = args["random"]
    size = args["vertices"]
    maximum_edges_number = args["edges"]
    algorithm = args["algorithm"]

    if seed:
        g = Graph().random_graph(size, seed, maximum_edges_number)
    else:
        g = Graph().read_graph(args["file"].name)
    
    minimum_weighted_closure = g.find_minimum_weighted_closure(algorithm = algorithm)
    print("\nMinimum Weighted Closure:", minimum_weighted_closure)

    if args["draw"]: g.draw_graph()

    plot.show()