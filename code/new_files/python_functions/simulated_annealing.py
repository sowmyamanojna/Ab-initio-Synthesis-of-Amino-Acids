import math

def get_exp_number_bonds(cycle, max_cycle, max_bonds):
	# Function imitates a Michaelis-Menten curve
	# for the number of bonds allowable at a 
	# given cycle and ceils the value returned.
	s = cycle/max_cycle
	bond = math.ceil((max_bonds*s)/(0.5 + s))
	
	return bond

def simulated_annealing():