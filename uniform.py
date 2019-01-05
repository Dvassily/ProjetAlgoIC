import networkx as nx
from random import random
import matplotlib.pyplot as plt
import numpy as np

def uniforme(a,b):
    return int(a+(b-a)*random())


def instances(n=1, t=1):
    complexes = list()
    size = uniforme(1, n)
    for i in range(t):
        subcomplex = list()
        j=0
        while j <size:
            node = np.random.choice(range(n))
            if node not in subcomplex :
                subcomplex.append(node)
                j+=1
        complexes.append(subcomplex)
    return complexes



complexes = instances(100, 6)
print(complexes)