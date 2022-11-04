from graph import Graph

def compute_results(
    maximum_nodes_number: int, 
    maximum_edges_number: list, 
    algorithm: str):

    data = dict()
    for m in maximum_edges_number:
        for n in range(1, maximum_nodes_number + 1):
            g = Graph().random_graph(n, 93107, m)
            minimum_weighted_closure, iterations, execution_time, solutions_number = \
                g.find_minimum_weighted_closure(algorithm = algorithm)
            
            #print("\n\nNumber of nodes: ", n)
            #print("Maximum number of edges: ", m)
            #print("Iterations: ", iterations)
            #print("Number of solutions found: ", solutions_number)
            #print("Minimum Weighted Closure:", minimum_weighted_closure)
            #print("Execution time: ", execution_time)

            data[n] = [
                iterations, 
                solutions_number, 
                minimum_weighted_closure, 
                execution_time
            ]

        with open("results/" + algorithm + "_search/" + str(m) + ".txt", 'w') as file:
            file.write(
                "{0:20s} {1:15s} {2:30s} {3:20s} {4:30s} \n".format(
                    "Number of nodes", 
                    "Iterations",
                    "Number of solutions found",
                    "Execution time",
                    "Minimum Weighted Closure",
                )
            )
            for n in data.keys():
                file.write(
                "{0:<20d} {1:<15d} {2:<30d} {3:<20f} {4:<30s} \n".format(
                    n,
                    data[n][0], 
                    data[n][1],  
                    data[n][3],
                    str(data[n][2]), 
                )
            )
            

if __name__ == '__main__':
    maximum_nodes_number = 20
    maximum_edges_number = [0.125, 0.25, 0.5, 0.75]

    compute_results(maximum_nodes_number, maximum_edges_number, "exhaustive")
    compute_results(maximum_nodes_number, maximum_edges_number, "greedy")

