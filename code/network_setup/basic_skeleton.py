import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_node('C')
G.add_node('H1')
G.add_node('H2')
G.add_node('H3')
G.add_node('H4')

G.add_edge('C', 'H1')

nx.draw(G, with_labels=True)
plt.show()