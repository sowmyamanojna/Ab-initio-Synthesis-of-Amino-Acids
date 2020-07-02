import os
import csv
import urllib
from bs4 import BeautifulSoup as bs
from rmg_parser import rmg_link_lists
from rmg_all_libraries import get_library_webpages

def write_soup(i, path_lib):
	url = f"https://rmg.mit.edu/database/thermo/libraries/{lib}/{i}/"
	html = (urllib.request.urlopen(url)).read()
	soup = bs(html, 'lxml')
	
	if os.getcwd() != path_lib:
		os.chdir(path_lib)
	if not os.path.exists("html"): 
		os.mkdir("html")
	os.chdir("html")

	name = f"{i}.html"
	fout = open(name, "w")
	fout.write(str(soup))
	fout.close()

def write_csv(num, path_lib):
	in_name = f"{num}.html"
	fin = open(in_name)
	data = fin.read()
	fin.close()

	soup = bs(data, "lxml")
	tr_list = soup.find_all("tr")
	td_list = []
	for i in tr_list:
		tds = i.find_all("td")
		td_list.append(tds)

	td_mapping = {"temp_start": [], "temp_end": [], "a_2":[], "a_1":[], "a0":[], "a1":[], "a2":[], "a3":[], "a4":[], "a5":[], "a6":[]}

	ref_list = ["temp_start", "temp_end", "a_2", "a_1", "a0", "a1", "a2", "a3", "a4", "a5", "a6"]
	td_list = soup.find_all("td")
	
	start1 = float(td_list[2].text.split()[0])
	end1 = float(td_list[2].text.split()[2])
	start2 = float(td_list[3].text.split()[0])
	end2 = float(td_list[3].text.split()[2])
	td_mapping[ref_list[0]].append(start1)
	td_mapping[ref_list[0]].append(start2)
	td_mapping[ref_list[1]].append(end1)
	td_mapping[ref_list[1]].append(end2)
	
	td_list = td_list[4:40]
	ref_list = ref_list[2:]
	
	# for i,j in enumerate(td_list):
	# 	print(i, "\t", j.text)

	for i,j in enumerate(td_list):
		if i%4 == 2 or i%4 == 3 :
			if "{" not in j.text:
				td_mapping[ref_list[i//4]].append(float(j.text))
			else:
				man = float(j.text.split()[0])
				exp = int(j.text.split()[2].split("{")[-1][:-1])
				td_mapping[ref_list[i//4]].append(float(man*10**exp))

	# for i in td_mapping:
	# 	print(i, td_mapping[i])

	if os.getcwd() != path_lib:
		os.chdir(path_lib)
		if not os.path.exists("csv"): 
			os.mkdir("csv")
		os.chdir("csv")

	fout = open(f"{num}.csv", "w")
	writer = csv.writer(fout)
	for i in td_mapping:
		writer.writerow(td_mapping[i])
	fout.close()

link_lists = rmg_link_lists()
print(link_lists)
# Considering only thoses compounds that have data in
# the NASA format

# link_lists = ["primaryThermoLibrary", "GRI-Mech3.0", "SABIC_aromatics", "surfaceThermoPt", "NOx2018", "JetSurF1.0", "surfaceThermoNi", "SulfurGlarborgMarshall", "NitrogenCurran", "Klippenstein_Glarborg2016", "primaryNS"]

# link_lists = ["CurranPentane", "USC-Mech-ii", "JetSurF2.0", "FFCM1(-)", "Lai_Hexylbenzene", "SulfurHaynes", "BurcatNS", "Chernov"]
path_base = os.getcwd()
for lib in link_lists:
	os.chdir(path_base)

	print(lib)
	mappings = get_library_webpages(lib)
	if not os.path.exists(f"{lib}_data"): 
		os.mkdir(f"{lib}_data")
	os.chdir(f"{lib}_data")
	path_lib = os.getcwd()

	for i in mappings:
		print("Compound", i)
		os.chdir(path_lib)	
		if not os.path.exists(f"csv/{i}.csv"):
			if not os.path.exists(f"html/{i}.html"): write_soup(i, path_lib)
			write_csv(i, path_lib)
		else:
			name = f"{lib}_data/{i}.csv"
			print(name, "already exists. Moving to next compound")
	if not os.listdir(): 
		os.chdir(path_base)
		os.rmdir(f"{lib}_data")