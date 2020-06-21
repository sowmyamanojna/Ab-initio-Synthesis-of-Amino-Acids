import networkx as nx

def get_accl(G):
	atoms = []
	compounds = []
	connected_components = nx.connected_components(G)
	list_compounds = list(connected_components)

	for i in list_compounds:
		if len(list(i)) == 1:
			atoms.append(list(i)[0])
		else:
			compounds.append(list(i))
	complete_list = []
	complete_list.extend(atoms)
	complete_list.extend(compounds)

	return atoms, compounds, complete_list