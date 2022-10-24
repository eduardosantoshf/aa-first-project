import argparse
from hashlib import algorithms_available
import matplotlib.pyplot as plot
from graph import SearchGraph

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
    parser.add_argument('-v',
        '--vertices', 
        metavar = 'N', 
        default = 25, 
        type = int, 
        required = False,
        help = 'number of vertices of the graph (default: %(default)s)'
    )
    parser.add_argument('-a', 
        '--algorithm', 
        metavar = 'NAME', 
        default = 'exhaustive', 
        type = str, 
        required = False,
        choices = ['exhaustive', 'branch-and-bound','greedy', 'astar', 'astar-heap'],
        help = 'number of vertices of the graph (default: %(default)s)'
    )
    parser.add_argument('-hr',
        '--heuristic', 
        metavar = 'N', 
        default = 1, 
        type = int, 
        required = False,
        help = 'heuristic used by the Greedy and A-star approach: '
            '(1) based on weights, (2) based on weights-degree,'
            ' (default: %(default)s)')

    args = vars(parser.parse_args())

    seed = args["random"]
    size = args["vertices"]
    algorithm = args["algorithm"]
    heuristic = args["heuristic"]

    if seed:
        g = SearchGraph().random_graph(size, seed)
    else:
        g = SearchGraph().read_graph(args["file"].name)

    g.draw_graph()

    plot.axis('on')
    plot.xlim(0, 10)
    plot.ylim(0, 10)
    plot.tick_params(left=True, bottom=True,             labelleft=True, labelbottom=True)
    plot.show()