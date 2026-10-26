import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    dot = 0.0
    norm_a_sq = 0.0
    norm_b_sq = 0.0
    for xi, yi in zip(a, b):
        dot += xi * yi
        norm_a_sq += xi * xi
        norm_b_sq += yi * yi

    norm_a = norm_a_sq ** (1/2)
    norm_b = norm_b_sq ** (1/2)
    
    if norm_a == 0 or norm_b == 0:
        return 0.0
    
    res = dot / (norm_a * norm_b)
    return res

