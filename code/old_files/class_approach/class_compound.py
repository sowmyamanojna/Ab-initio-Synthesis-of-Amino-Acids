import networkx as nx
import matplotlib.pyplot as plt

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


if __name__ == "__main__":
	C1 = Compound("C", 1)
	print(C1)