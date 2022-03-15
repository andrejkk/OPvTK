# @brief At least two functions must be provided:
#  1. Main function of the algorithm
#  2. is_correctQ(x, y)  function returning True for correct results and false otherwise where x is coplete input and y complete output data of the algorithm


import numpy as np


# @brief It returns square root
# @par x input parameter
# @return square roor
def sq_root(x):

    return np.sqrt(x) + 1



# @brief Test result correctness
# @par x input data
# @par output data
# @return correctQ True if correct and false otherwise
def is_correctQ(x, y):
    
    correctQ = True
    
    if np.abs(y*y - x) > 0.001:
        correctQ = False
    
    return correctQ