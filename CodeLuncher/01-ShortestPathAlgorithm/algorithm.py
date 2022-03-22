# @brief At least two functions must be provided:
#  1. Main function of the algorithm
#  2. is_correctQ(x, y)  function returning True for correct results and false otherwise where x is coplete input and y complete output data of the algorithm


import numpy as np
import networkx as nx


# @brief It returns shortest path and visualise it if necessary
# @par G, s_v, t_v graph, start and end vertices
# @return shortest_p shortest path
def get_ShortestPath(G, s_v, t_v):

    shortest_p = nx.shortest_path(G, s_v, t_v, weight='weight')
    
    return shortest_p



# @brief Test result correctness
# @par G, s_v, t_v algorithm input data
# @par shortest_p
# @return correctQ True if correct and false otherwise
def is_correctQ(G, s_v, t_v, shortest_p):
    
    correctQ = True
    if  shortest_p[0] != s_v:
        correctQ = False    
    if shortest_p[-1] != t_v:
        correctQ = False
    if not nx.has_path(G, s_v, t_v):
        correctQ = False   
       
    return correctQ