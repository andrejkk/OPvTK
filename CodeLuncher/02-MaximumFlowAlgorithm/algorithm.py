# @brief At least two functions must be provided:
#  1. Main function of the algorithm
#  2. is_correctQ(x, y)  function returning True for correct results and false otherwise where x is coplete input and y complete output data of the algorithm


import numpy as np
import networkx as nx


# @brief It returns shortest path and visualise it if necessary
# @par G, s_v, t_v graph, start and end vertices
# @return shortest_p shortest path
def get_MaximalFlow(G, s_v, t_v):

    flow_value, flow_dict = nx.maximum_flow(G, s_v, t_v)
    
    return flow_value, flow_dict



# @brief Test result correctness
# @par G, s_v, t_v algorithm input data
# @par shortest_p
# @return correctQ True if correct and false otherwise
def is_correctQ(G, s_v, t_v, flow_value, flow_dict):
    
    correctQ = True
    
    start_flow = sum([flow_dict[s_v][x] for x in flow_dict[s_v]])

    
    # Flow goes from starting node?
    if np.abs(start_flow - flow_value) > 0.01:
        correctQ = False

    # Capacities are not exceeded?
    for e in G.edges():
        u,v = e[0], e[1]
        if flow_dict[u][v] > G[u][v]['capacity']:
            correctQ = False
        
     
       
    return correctQ