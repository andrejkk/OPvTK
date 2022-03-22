# @brief Benchmarks for Shortest path to select / generate data 


import numpy as np
import networkx as nx


# @brief get shortest path of a given directed graph
# @par params_lst list of parameters params_lst=['Name', ... , plotQ] where 'Name' is a benchmark name, ... stands for aditional parameters and the last one is plotQ (plot benchmark or not) 
def get_shortestPathAlg_benchmark(params_lst):

    plotQ = params_lst[-1]
    
    
    if params_lst[0] == "Custom_5": # Custom graph 5 points
        
        # Directed graph
        G = nx.DiGraph()
        weights = [(1, 2, 4.0), (1, 3, 10.0), (2, 3, 3.0), (2, 4, 2.0),
                   (3, 4, 4.0), (3, 5, 6.0), (4, 5, 5.0)]
        G.add_weighted_edges_from(weights)
        
        # Start and termination node
        s_v, t_v = 1, 5
        
        
    if params_lst[0] == "K_n": # Full graph 
        
        # Directed graph
        n = params_lst[1]
        G = nx.complete_graph(n, create_using=nx.DiGraph)

        # Start and termination node
        s_v, t_v = 0, n-1
        

    # Plot
    if plotQ:
        # Draw it
        pos=nx.planar_layout(G) # graphviz_layout(G) 
        nx.draw_networkx(G, pos)
        weights = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    
    
    
    return G, s_v, t_v