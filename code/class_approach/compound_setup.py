import matplotlib.pyplot as plt
import networkx as nx
from class_compound import Compound

H_list = [Compound("H", i) for i in range(1,33)]
C_list = [Compound("C", i) for i in range(33, 41)]
O_list = [Compound("O", i) for i in range(41, 49)]
N_list = [Compound("N", i) for i in range(49, 57)]

G = nx.Graph()
for i,lst in enumerate([H_list, C_list, O_list, N_list]):
	for comp in lst:
		G.add_node(comp._name, data=comp)
nx.draw(G, with_labels=True)
plt.show()



nx.add_edge("H1", "N1", "H2", "H3")