#Initial set up 
import networkx as nx

G = nx.Graph()
initial_H = ['H']*32
initial_C = ['C']*8
initial_O = ['O']*8
initial_N = ['N']*8
initial_comp = initial_H
for i in range(len(initial_C)):
    initial_comp.append(initial_C[i])
    initial_comp.append(initial_O[i])
    initial_comp.append(initial_N[i])
for i in range(len(initial_comp)):
    G.add_node(i+1, name = initial_comp[i])

#Test
G.add_edge(1,2)
G.add_edge(50,51)

#List of nodes with names
nodes_list = list(G.nodes(data='name'))

#List of connected components
H = nx.connected_components(G)
H = list(H)
n = len(H)
conn_comp = []
for i in range(n):
    conn_comp.append(list(H[i]))

elements = []
compounds = []
for i in range(n):
    if len(conn_comp[i])==1:
        elements.append(conn_comp[i])
    else:
        compounds.append(conn_comp[i])

print('Elements')
print(elements)
print('Compounds')
print(compounds)

nx.draw(G,with_labels=True)