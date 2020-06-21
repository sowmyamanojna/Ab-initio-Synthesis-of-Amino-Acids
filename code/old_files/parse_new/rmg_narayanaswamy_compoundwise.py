import os
import csv
import urllib
from bs4 import BeautifulSoup as bs
from rmg_narayanaswamy import get_narayanaswamy_webpages

def write_soup(i):
	url = f"https://rmg.mit.edu/database/thermo/libraries/Narayanaswamy/{i}/"
	html = (urllib.request.urlopen(url)).read()
	soup = bs(html, 'lxml')

	if os.getcwd() != "/home/sowmya/Desktop/bt5240/project/code/get_data_rmg/Narayanaswamy_data/":
		os.chdir("/home/sowmya/Desktop/bt5240/project/code/get_data_rmg/Narayanaswamy_data/")
		if not os.path.exists("html"): 
			os.mkdir("html")
		os.chdir("html")

	name = f"{i}.html"
	fout = open(name, "w")
	fout.write(str(soup))
	fout.close()

def write_csv(num):
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

	# out_name = f"{num}.csv"
	# fout = open(out_name, "w")
	# writer = csv.writer(fout)
	# writer.writerows(td_list)
	# fout.close()

	td_mapping = {"a_2":[], "a_1":[], "a0":[], "a1":[], "a2":[], "a3":[], "a4":[], "a5":[], "a6":[]}

	ref_list = ["a_2", "a_1", "a0", "a1", "a2", "a3", "a4", "a5", "a6"]
	td_list = soup.find_all("td")
	td_list = td_list[4:-9]
	for i,j in enumerate(td_list):
		if i%4 == 2 or i%4 == 3 :
			if "{" not in j.text:
				td_mapping[ref_list[i//4]].append(float(j.text))
			else:
				man = float(j.text.split()[0])
				exp = int(j.text.split()[2].split("{")[-1][:-1])
				td_mapping[ref_list[i//4]].append(float(man*10**exp))

	if os.getcwd() != "/home/sowmya/Desktop/bt5240/project/code/get_data_rmg/Narayanaswamy_data/":
		os.chdir("/home/sowmya/Desktop/bt5240/project/code/get_data_rmg/Narayanaswamy_data/")
		if not os.path.exists("csv"): 
			os.mkdir("csv")
		os.chdir("csv")

	fout = open(f"{num}.csv", "w")
	writer = csv.writer(fout)
	for i in td_mapping:
		writer.writerow(td_mapping[i])
	fout.close()


mappings = get_narayanaswamy_webpages()
if not os.path.exists("Narayanaswamy_data"): 
	os.mkdir("Narayanaswamy_data")
	os.chdir("Narayanaswamy_data")

for i in mappings:
	print("Compound", i)
	os.chdir("/home/sowmya/Desktop/bt5240/project/code/get_data_rmg/Narayanaswamy_data/")	
	if not os.path.exists(f"/csv/{i}.csv"):
		write_soup(i)
		write_csv(i)
	else:
		name = f"Narayanaswamy_data/{i}.csv"
		print(name, "already exists. Moving to next compound")

