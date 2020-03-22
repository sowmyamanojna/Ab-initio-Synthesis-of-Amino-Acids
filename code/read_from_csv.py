import csv
import os
import numpy as np
import scipy.constants as sc
# from rmg_parser import rmg_link_lists

def calculate_H(data, T):
	[a_2, a_1, a0, a1, a2, a3, a4, a5, _] = data

	H = sc.R*T*(-a_2*T**-2 + a_1*T**-1*np.log(T) + a0 + 0.5*a1*T + (a2*T**2)/3 + 0.25*a3*T**3 + 0.2*a4*T**4 +a5*T**-1)
	return H

def calculate_S(data, T):
	[a_2, a_1, a0, a1, a2, a3, a4, _, a6] = data

	S = sc.R*(-0.5*a_2*T**-2 - a_1*T**-1 + a0*np.log(T) + a1*T + 0.5*a2*T**2 + (a3*T**3/3) + 0.25*a4*T**4 + a6)

	return S

def calculate_G(H, S, T):
	G = H - T*S
	return G

def read_from_csv(libraries_list, temperature, path):
	# libraries_list = rmg_link_lists()

	H_lists = []
	S_lists = []
	G_lists = []

	H_list = []
	S_list = []
	G_list = []

	for lib in libraries_list:
		os.chdir(path)

		compound_list = os.listdir()		

		directory = f"{lib}_data"
		if os.path.exists(f"{directory}/csv"):
			print("CSV folder exists")
			os.chdir(f"{directory}/csv")
		
			compound_list = os.listdir()

			for file_name in compound_list:
				fin = open(file_name)
				reader = csv.reader(fin)
				data = []
				if (temperature > 100 and temperature < 1074.56):
					for i in reader:
						data.append(float(i[0]))
				else:
					for i in reader:
						data.append(float(i[1]))

				H = calculate_H(data, temperature)
				S = calculate_S(data, temperature)
				G = calculate_G(S, H, temperature)

				H_list.append(H)
				S_list.append(S)
				G_list.append(G)

			H_lists.append(H_list)
			S_lists.append(S_list)
			G_lists.append(G_list)

	return [H_lists, S_lists, G_lists]

if __name__ == "__main__":
	path = os.getcwd()
	libraries_list = ['primaryThermoLibrary', 'DFT_QCI_thermo', 'GRI-Mech3.0', 'CBS_QB3_1dHR', 'thermo_DFT_CCSDTF12_BAC', 'SABIC_aromatics', 'C3', 'Fulvene_H', 'BurkeH2O2', 'Chlorinated_Hydrocarbons', 'Narayanaswamy', 'CHN', 'surfaceThermoPt', 'vinylCPD_H', 'SulfurGlarborgH2S', 'naphthalene_H', 'NOx2018', 'iodinated_Hydrocarbons', 'JetSurF1.0', 'surfaceThermoNi', 'SulfurGlarborgMarshall', 'CH', 'NitrogenCurran', 'CHO', 'bio_oil', 'SulfurLibrary', 'C10H11', 'Klippenstein_Glarborg2016', 'primaryNS', 'CurranPentane', 'USC-Mech-ii', 'GRI-Mech3.0-N', 'JetSurF2.0', 'FFCM1(-)', 'SulfurGlarborgNS', 'NISTThermoLibrary', 'Lai_Hexylbenzene', 'SulfurHaynes', 'CN', 'BurcatNS', 'SulfurGlarborgBozzelli', 'Chernov', 'CHON']

	[H_lists, S_lists, G_lists] = read_from_csv(libraries_list, 700, path)
	
	for lib,H_list,S_list,G_list in zip(libraries_list, H_lists, S_lists, G_lists):
		print(lib)

		for H, S, G in zip(H_list, S_list, G_list):
			print("%.2f" %H, end="\t\t")
			print("%.2f" %S, end="\t\t")
			print("%.2f" %G)