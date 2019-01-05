import networkx as nx
import numpy as np

def build_sub_matrix(subcomplexes, node_number=100):
    node_matrix = np.zeros((node_number, subcomplexes.shape[0]))
    for v in range(node_number):
        for m in subcomplexes:
            if v in m:
                node_matrix[v][m] = 1

    return node_matrix


def build_node_matrix(sub_matrix):
    node_matrix = np.empty(sub_matrix.shape)
    for v in range(sub_matrix.shape[0]):
        for m in range(sub_matrix.shape[1]):
            if sub_matrix[v][m] == 1 :
                node_matrix[v][m] = v
    return node_matrix

def greedy_merge(subcomplexes, shape=(100, 1)):
    sub_matrix = build_sub_matrix(subcomplexes, shape[0])
    node_matrix = build_node_matrix(sub_matrix)
    contrib_matrix = np.empty(shape[0], dtype=int)

    for v in range(shape[0]):
        for w in range(v:shape[0]):
            contrib = 0
            for m in range(subcomplexes):
                


    
