import csv
import os
import numpy as np
import scipy.constants as sc
from rmg_parser import rmg_link_lists

def calculate_H(data, T):
	[a_2, a_1, a0, a1, a2, a3, a4, a5, _] = data

	H = sc.R*T(-a_2*T**-2 + a_1*T**-1*np.log(T) + a0 + 0.5*a1*T + (a2*T**2)/3 + 0.25*a3*T**3 + 0.2*a4*T**4 +a5*T**-1)
	return H

def calculate_S(data, T):
	[a_2, a_1, a0, a1, a2, a3, a4, _, a6] = data

	S = sc.R*(-0.5*a_2*T**-2 - a_1*T**-1 + a0*np.log(T) + a1*T + 0.5*a2*T**2 + (a3*T**3/3) + 0.25*a4*T**4 + a6)

	return S

def calculate_G(H, S, T):
	G = H - T*S
	return G

def read_from_csv(temperature):
	libraries_list = rmg_link_lists()
	for lib in libraries_list:
		os.chdir("/home/sowmya/Desktop/bt5240/project/code/get_data_rmg/")

		directory = f"{lib}_data/csv"
		if os.path.exists(directory):
			os.chdir(directory)
		compound_list = os.listdir()

		for file_name in compound_list:
			fin = open(file_name)
			reader = csv.reader(fin)
			data = []
			if (temperature > 100 and temperature < 1074.56):
				for i in reader:
					data.append(i[0])
			else:
				for i in reader:
					data.append(i[1])

			H = calculate_H(data, temperature)
			S = calculate_S(data, temperature)
			G = calculate_G(S, H, temperature)

	return [H, S, G]