import networkx as nx

def is_valid(graph, subcomplexes):
    for sc in subcomplexes:
        sg = graph.subgraph(sc)
        is_connected = len(list(nx.connected_components(sg))) == 1

        if not is_connected:
            return False

    return True

def _compute_graphs(graph, edges):
    l = []

    if len(edges) == 0:
        l.append(graph)
        return l
    else:
        print(len(edges))
    
    for e in edges:
        u = e[0]
        v = e[1]

        g1 = graph.copy()
        g2 = graph.copy()
        
        if g1.has_edge(u, v):
            g1.remove_edge(u, v)
                
        if g1.has_edge(v, u):
            g1.remove_edge(v, u)

        l += _compute_graphs(g1, edges[1:])
        l += _compute_graphs(g2, edges[1:])

    return l

def compute_graphs(n):
    graph = nx.complete_graph(n)
    edges = []

    for u,v in nx.edges(graph):
        edges.append((u, v))
    
    return _compute_graphs(graph, edges)

if __name__ == '__main__':
    n = 4
    
    subcomplexes = [ [0, 1, 2], [3, 4, 5], [6, 7, 8, 9], [10, 11, 12], [12, 13], [13, 0], [0, 3, 6, 10], [1, 5, 8, 11], [2, 3, 7, 12] ]

    # for n in graph.node:
    #     print(n)

    graphs = compute_graphs(n)
    
    print(len(graphs))
    
