# @brief Benchmarks for Maximal flow to select / generate data 


import numpy as np
import networkx as nx


# @brief get shortest path of a given directed graph
# @par params_lst list of parameters params_lst=['Name', ... , plotQ] where 'Name' is a benchmark name, ... stands for aditional parameters and the last one is plotQ (plot benchmark or not) 
def get_cliqueAlg_benchmark(params_lst):
    
    
    # nx.generators.small.
    # nx.gnp_random_graph(10, 0.3, 138)

    plotQ = params_lst[-1]
    
    
    # Custom graph 5 points
    if params_lst[0] == "Custom_5": 
    
        G = nx.Graph()
        G.add_edge(1, 2, capacity=4.0)
        G.add_edge(1, 3, capacity=5.0)
        G.add_edge(2, 3, capacity=3.0)
        G.add_edge(2, 4, capacity=6.0)
        G.add_edge(3, 4, capacity=2.0)
        G.add_edge(3, 5, capacity=8.0)
        G.add_edge(4, 5, capacity=3.0)
        
       
        #pos=nx.planar_layout(G)
        #nx.draw_networkx_edges(G,pos)
        
    # Full graph 
    if params_lst[0] == "K_n": 
        
        # Directed graph
        n = params_lst[1]
        G = nx.complete_graph(n, create_using=nx.Graph)
        
        
    
    # Random graph
    if params_lst[0] == "RND":
        n, p = params_lst[1], params_lst[2]
        
        # Random graph
        G = nx.gnp_random_graph(n, p, directed=False)
        
       
        

    # Plot
    if plotQ:
        # Draw it
        pos=nx.planar_layout(G) # graphviz_layout(G) 
        nx.draw_networkx(G, pos)
        
        
    return G

