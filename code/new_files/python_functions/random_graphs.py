import random
import numpy as np
import networkx as nx

def generate_random_graphs(G,bonds):
    nodes = list(nx.nodes(G))
    connected_components = nx.connected_components(G)
    A = nx.adjacency_matrix(G)
    bonds -= nx.number_of_edges(G)
    
    print(nx.number_of_edges(G))
    
    while nx.number_of_edges(G) < bonds:
        row = random.randint(1,55)
        cur_val1 = (nodes[row])._valency
        
        while not(cur_val1 > 0):
            row = random.randint(1,55)
            cur_val1 = nodes[row]._valency
        else:
            col = random.randint(0, row-1)
            cur_val2 = nodes[col]._valency
            while not(cur_val2 > 0):
                col = random.randint(0, row-1)
                cur_val2 = nodes[col]._valency
                if cur_val2 > 0:
                    G.add_edge(nodes[row], nodes[col])
            else:
                G.add_edge(nodes[row], nodes[col])
                G.add_edge(nodes[row], nodes[col])
            
        for i in list(nx.nodes(G)): 
            i.current_valency(G)
    return G

if __name__ == "__main__":
    generate_random_graphs(G, p, bonds)