# To get connected components in an iterable fashion

import networkx as nx
G = nx.Graph()
G.add_edges_from([(0,1),(1,2),(2,3),(5,6)])
H = nx.connected_components(G)
H = list(H)
n = len(H)
conn_comp = []
for i in range(n):
    conn_comp.append(list(H[i]))
print(conn_comp)