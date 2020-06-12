import matplotlib.pyplot as plt
import networkx as nx

class Compound():
    def __init__(self, name, number):
        self._name = name + " " + str(number)
        self._number = number
        self._valency = self.get_valence()

    def get_valence(self):
        name = self._name.split()[0]
        if name == "H":
            return 1
        elif name == "C":
            return 4
        elif name == "N":
            return 3
        elif name == "O":
            return 2

    def __repr__(self):
        G = nx.Graph()
        G.add_node(self._name, data = self)
        nx.draw(G, with_labels=True)
        plt.show()
        return self._name
    
    def update_valency(self, val):
        self._valency += val

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

G.add_edges_from([('H 1', 'N 49'), ('N 49', 'H 2'), ('N 49','H 3')])

"""
This ain't working
Me not able to update valencies
"""

nx.draw(G, with_labels=True)
plt.show()