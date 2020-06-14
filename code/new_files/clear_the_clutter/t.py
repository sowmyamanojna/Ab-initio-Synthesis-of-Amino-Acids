import os
import csv
from bs4 import BeautifulSoup as bs

os.chdir("narayanaswamy_data")
fin = open("1.csv")
data = fin.read()
fin.close()

soup = bs(data,"lxml")

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

print(td_mapping)

fout = open("1.csv", "w")
writer = csv.writer(fout)
for i in td_mapping:
	writer.writerow(td_mapping[i])
fout.close()