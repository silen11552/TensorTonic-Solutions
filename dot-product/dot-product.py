import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    
    pass
    res=0.0
    for xi,yi in zip(x,y):
        res +=xi*yi
    return res
    x=[float(i) for i in input().spilt(',') ]
    y=[float(i) for i in input().spilt(',') ]