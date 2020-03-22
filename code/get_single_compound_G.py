import os
import csv
from read_from_csv import calculate_G, calculate_S, calculate_H


def read_from_csv(lib, temperature, path, file_name):
	H_list = []
	S_list = []
	G_list = []

	os.chdir(path)	

	directory = f"{lib}_data"
	if os.path.exists(f"{directory}/csv"):
		print("CSV folder exists")
		os.chdir(f"{directory}/csv")
		
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
		G = calculate_G(H, S, temperature)

	return [H, S, G]

if __name__ == "__main__":
	lib = "BurcatNS"
	path = os.getcwd()
	temperature = 273
	file_name = "46.csv"

	result = read_from_csv(lib, temperature, path, file_name)

	for i in result:
		print(i)


	lib = "GRI-Mech3.0"
	file_name = "15.csv"
	temperature = 273

	result = read_from_csv(lib, temperature, path, file_name)

	for i in result:
		print(i)
