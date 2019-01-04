import networkx as nx
import random
from random import choice

def uniforme(a,b):
    return(a+(b-a)*random())


def build_subcomplex(size, graph):
    subcomplex = list()
    random_node = choice(graph.nodes())
    subcomplex.append(random_node)
    while len(subcomplex)<size:
        random_node = choice(nx.all_neighbors(graph, random_node))
        subcomplex.append(random_node)
    return subcomplex

def build_full_graph(n):
    return nx.gnp_random_graph(n, 0.2)

def instances(n=1, t=1):
    #Build a graph of size n
    graph = build_full_graph(n)
    subcomplexes = list()
    for i in range(t):
        subcomplexes.append(build_subcomplex(uniforme(1, n), graph))
    
    return graph, subcomplexes

    

