import networkx as nx

def is_valid(graph, subcomplexes):
    is_connected = len(list(nx.connected_components(graph))) == 1
    has_isolates = len(list(nx.isolates(graph))) > 0
    
    if (not is_connected)  or has_isolates or (len(nx.edges(graph)) == 0):
        return False
    
    for sc in subcomplexes:
        sg = graph.subgraph(sc)
        is_connected = len(list(nx.connected_components(sg))) == 1

        if not is_connected:
            return False

    return True

def _compute_graphs(graph, edges, start, n):
    l = []

    if len(edges) == 0:
        l.append(graph)
        return l

    e = edges[0]
    u = e[0]
    v = e[1]

    g1 = graph.copy()
    g2 = graph.copy()
        
    if g1.has_edge(u, v):
        g1.remove_edge(u, v)
        
    l += _compute_graphs(g1, edges[1:], start + 1, n)
    l += _compute_graphs(g2, edges[1:], start + 1, n)

    return l

def compute_graphs(n):
    graph = nx.complete_graph(n)
    edges = []

    for u,v in nx.edges(graph):
        edges.append((u, v))
    
    graphs = _compute_graphs(graph, edges, 0, n)

    return graphs
                
if __name__ == '__main__':
    n = 6
    
    subcomplexes = [ [0, 1], [2, 3], [4, 5], [0, 2, 4], [1, 3, 5] ]

    glustres = list()
    for gla in compute_graphs(n):
        if is_valid(gla, subcomplexes):
            glustres.append(gla)

    
    ming = None
    for glu in glustres:
        e = nx.edges(glu)

        if ming is None or len(e) < len(nx.edges(ming)):
            print(len(list(nx.isolates(glu))))
            ming = glu

    print(len(nx.edges(ming)))
    print(nx.edges(ming))

