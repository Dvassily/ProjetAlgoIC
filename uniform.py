import networkx as nx
from random import choice, random
import matplotlib.pyplot as plt
import numpy as np

def uniforme(a,b):
    return int(a+(b-a)*random())


def build_subcomplex(size, graph):
    subcomplex = list()
    random_node = np.random.choice(graph.nodes())
    subcomplex.append(random_node)
    while len(subcomplex)<size:
        random_node = np.random.choice(list(graph.neighbors(random_node)))
        if random_node not in subcomplex : subcomplex.append(random_node) 
    return subcomplex

def build_full_graph(n):
    return nx.complete_graph(n)

def instances(n=1, t=1):
    #Build a graph of size n
    graph = build_full_graph(n)
    subcomplexes = list()
    for i in range(t):
        subcomplexes.append(build_subcomplex(uniforme(1, n), graph))
    
    return graph, subcomplexes



graph, subcomplexes = instances(100, 2)
nx.draw(graph)
plt.show()
print(subcomplexes)
    

