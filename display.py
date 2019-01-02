import matplotlib.pyplot as plt
import networkx as nx
import random

if __name__ == '__main__':
    n = 100
    
    graph = nx.complete_graph(n)

    edges = graph.number_of_edges()


    i = 0
    while i < int(edges * 0.95):
        edge = random.choices(list(graph.edges))[0]
        
        graph.remove_edge(edge[0], edge[1])

        is_connected = len(list(nx.connected_components(graph))) == 1
        
        if not is_connected:
            graph.add_edge(edge[0], edge[1])
        else:
            i += 1
            
    plt.subplot(111)
    nx.draw(graph)
    plt.show()

    
    

