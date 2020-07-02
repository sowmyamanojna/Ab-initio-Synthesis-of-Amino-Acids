import math
import random as r
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from compound_class import Compound
from fix_valencies import fix_valencies
from calculate_G_S_H import *
from get_data import *
from generate_initial_compounds import generate_initial_compounds
from get_atoms_compounds import get_accl
from random_graphs import generate_random_graphs

# Defining the atom list in the Graph
print('Defining the initial atoms ...')
H_list = [Compound("H", i) for i in range(1,33)]
C_list = [Compound("C", i) for i in range(33, 41)]
O_list = [Compound("O", i) for i in range(41, 49)]
N_list = [Compound("N", i) for i in range(49, 57)]


# Creating the graph with just atoms
print('Creating a graphical representation ...')
G = nx.MultiGraph()
for i,lst in enumerate([H_list, C_list, O_list, N_list]):
	for comp in lst:
		G.add_node(comp, data=comp)
plt.figure()
nx.draw(G, with_labels=True)
plt.show()

# Adding all the nodes
print('Generating all the initial compounds ...')
G = generate_initial_compounds(G, H_list, C_list, N_list)
fix_valencies(G)

nx.draw(G, with_labels=True)
plt.show()

# Get all the connected components in the graph
all_compounds = nx.connected_components(G)
print('The list of connected components:')
for compound in all_compounds:
	if len(compound) > 1: 
		print(compound)

print('Get the thermodynamic values for Ammonia:')
temperature = 700
path = os.getcwd()
# Details for NH3 (Ammonia)
# https://rmg.mit.edu/database/thermo/molecule/1%20N%20u0%20p1%20c0%20%7B2,S%7D%20%7B3,S%7D%20%7B4,S%7D%0A2%20H%20u0%20p0%20c0%20%7B1,S%7D%0A3%20H%20u0%20p0%20c0%20%7B1,S%7D%0A4%20H%20u0%20p0%20c0%20%7B1,S%7D%0A
ammonia_lib = "NOx2018"
ammonia_file_name = "65.csv"

(H_amm, S_amm, G_amm) = get_single_compound_data(ammonia_lib, temperature, path, ammonia_file_name)
print('H:', H_amm)
print('S:', S_amm)
print('G:', G_amm)


# Get the list of all compounds and atoms
print('Getting a list of all compounds and atoms ...')
atoms, compounds, complete_list = get_accl(G)

print('Getting the free electron distribution ...')
free_electrons = []
for i in complete_list:
	val = 0
	compound_contrib = {}
	if np.size(i) > 1:
		for j in i:
			compound_contrib[j] = j.get_total_valency(G)
			val += j.get_total_valency(G)
	else:
		compound_contrib[i] = i.get_total_valency(G)
		val += i.get_total_valency(G)
	free_electrons.append((val, compound_contrib))

print('Setting up parameters for Simulated Annealing ...')
minimum_energy = 1e10;
epochs = 100;

maximum_edges = 0; # 52
for lst in [H_list, C_list, O_list, N_list]:
	for atom in lst:
		maximum_edges += atom.get_max_valency()
		
maximum_edges = maximum_edges//2;

flag = input("Would you like to have a saturating bond formation? (y/n) ")
G = generate_random_graphs(G, maximum_edges)
nx.draw(G, with_labels=True)
plt.show()