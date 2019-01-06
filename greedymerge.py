import networkx as nx
import numpy as np

def build_sub_matrix(subcomplexes, node_number=100):
    sub_matrix = np.zeros((node_number, subcomplexes.shape[0]))
    
    for v in range(node_number):
        for m, s in enumerate(subcomplexes):
            if v in s:
                sub_matrix[v][m] = 1
    
    return sub_matrix

def build_node_matrix(sub_matrix):
    mat =  [ [ set() for x in range(sub_matrix.shape[1])] for y in range(sub_matrix.shape[0]) ]
    for v in range(sub_matrix.shape[0]):
        for m in range(sub_matrix.shape[1]):
            if sub_matrix[v][m] == 1 :
                mat[v][m].add(v)

    return mat 

def build_contrib_matrix(sub_matrix):
    contrib_matrix = [ [] for x in range(sub_matrix.shape[1]) ]
    
    for v in range(sub_matrix.shape[0]):
        for w in range(sub_matrix.shape[0]):
            if v > w:
                contrib = 0
                
                for m in range(sub_matrix.shape[1]):
                    if sub_matrix[v][m] == 1 and sub_matrix[w][m] == 1:
                        contrib += 1

                if contrib > 0:
                    contrib_matrix[contrib].append((v, w))

    return contrib_matrix
    
def greedy_merge(subcomplexes, node_number=100):
    result = []
    sub_matrix = build_sub_matrix(subcomplexes, node_number)
    node_matrix = build_node_matrix(sub_matrix)
    contrib_matrix = build_contrib_matrix(sub_matrix)

    highestContributor = 0
    for i in reversed(range(len(contrib_matrix))):
        if len(contrib_matrix[i]) != 0:
            highestContributor = i
            break

    print(node_matrix)

    while highestContributor > 0:
        v,w = contrib_matrix[highestContributor].pop(0)
        print("->" + str((v, w)))

        result.append((v, w))

        for m in range(sub_matrix.shape[1]):
            print(m)
            if sub_matrix[v][m] == 1 and sub_matrix[w][m] == 1:
                print('foo' + str(m))
                print(node_matrix[v][m])
                print(node_matrix[w][m])
                for v2 in node_matrix[v][m]:
                    for w2 in node_matrix[w][m]:
                        print((v2, w2), (v, w))
                        if not (v == v2 and w == w2):
                            print(v2, w2)
                            j = 0
                            e = None
                            for i, c in enumerate(contrib_matrix):
                                if e is None and (v2, w2) in c or (w2, v2) in c:
                                    j = i
                                    e = c
                                    
                            
                            if e is not None:
                                if (v2, w2) in e:
                                    e.remove((v2, w2))
                                if (w2, v2) in e:
                                    e.remove((w2, v2))
                                if j > 1:
                                    contrib_matrix[j - 1].append((v2, w2))
                
                tmp_subset = node_matrix[v][m].union(node_matrix[w][m])

                for v3 in tmp_subset:
                    node_matrix[v3][m] = tmp_subset

        for e in node_matrix:
            print(e)
        print(contrib_matrix)
        while highestContributor > 0 and len(contrib_matrix[highestContributor]) == 0:
            highestContributor = highestContributor - 1

    return result
    
if __name__ == '__main__':
    subcomplexes = np.array([[0, 1, 3], [0, 1, 2, 3], [1, 3, 4], [1, 4]])
    result = greedy_merge(subcomplexes, 5)
    print(result)
