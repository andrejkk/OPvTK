# @brief At least two functions must be provided:
#  1. Main function of the algorithm
#  2. is_correctQ(x, y)  function returning True for correct results and false otherwise where x is coplete input and y complete output data of the algorithm


import numpy as np
import networkx as nx


# @brief It returns shortest path and visualise it if necessary
# @par G, s_v, t_v graph, start and end vertices
# @return shortest_p shortest path
def get_Cliques(G):

    cliques_itr = nx.find_cliques(G)
    
    return cliques_itr



# @brief Test result correctness
# @par G algorithm input data
# @par cliques_itr
# @return correctQ True if correct and false otherwise
def is_correctQ(G, cliques_itr):

    cliques_lst = list(cliques_itr)
    
    correctQ = True
    
    # Are all cliques subgraphs?


    # Are all cliques full graphs?
     
       
    return correctQ