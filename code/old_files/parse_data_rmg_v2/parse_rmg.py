import os
import csv
import numpy as np
import pandas as pd
import urllib
from bs4 import BeautifulSoup as bs

def get_list_libraries():
	"""
	Gets the list of all names of all libraries
	present in the RMG database.

	The first four entries are ignored because they 
	stand for Home, ..., Libraries.
	"""
	html = (urllib.request.urlopen(base_url)).read()
	soup = bs(html, 'lxml')

	all_lis = soup.find_all('li')
	libraries = [li.a.text for li in all_lis if li.a]

	return libraries[4:]
		

def get_labelwise_data(label, lib):
	"""
	Get thermodynamic data of all compounds
	in which the data is in NASA format
	The data in the Group additivity format is
	represented in the form of Plotly graphs
	and hence, is difficult to parse.
	"""
	url = base_url + lib + "/" + label
	html = (urllib.request.urlopen(url)).read()
	soup = bs(html, 'lxml')

	all_tds = soup.find_all("td", class_='value')
	temp_range1 = all_tds[0].text
	temp_range2 = all_tds[1].text
	
	all_tds_first = all_tds[2:20:2]
	all_tds_second = all_tds[3:20:2]
	
	thermo_values1 = []
	thermo_values2 = []
	
	for td in all_tds_first:
		if '\\times' in td.text:
			text = td.text
			val = text.split('{')
			exp = float(val[-1][:-1])
			man = float(val[0].split()[0])
			thermo_values1.append(man*10**exp)
		else:
			thermo_values1.append(float(td.text))

	for td in all_tds_first:
		if '\\times' in td.text:
			text = td.text
			val = text.split('{')
			exp = float(val[-1][:-1])
			man = float(val[0].split()[0])
			thermo_values2.append(man*10**exp)
		else:
			thermo_values2.append(float(td.text))

	return temp_range1, temp_range2, thermo_values1, thermo_values2


def get_dataframe(lib):
	url = base_url + lib
	html = (urllib.request.urlopen(url)).read()
	soup = bs(html, 'lxml')

	print(lib)

	data = {'Database name':[], 'Label':[], 'Name':[], 'Temperature range 1': [], 'a_2':[], 'a_1':[], 'a0':[], 'a1':[], 'a2':[], 'a3':[], 'a4':[], 'a5':[], 'a6':[], 'Temperature range 2': [], 'a_2.2':[], 'a_1.2':[], 'a0.2':[], 'a1.2':[], 'a2.2':[], 'a3.2':[], 'a4.2':[], 'a5.2':[], 'a6.2':[]}

	all_trs = soup.find_all('tr')
	for tr in all_trs:
		all_tds = tr.find_all('td')
		if all_tds and all_tds[-1].text == "NASA":
			label = all_tds[0].a.text.split(".")[0]
			name = all_tds[0].a.text.split()[-1]
			print(label, name)
			data['Database name'].append(lib)
			data['Label'].append(label)
			data['Name'].append(name)

			temp_range1, temp_range2, thermo_values1, thermo_values2 = get_labelwise_data(label, lib)
			data['Temperature range 1'].append(temp_range1)
			data['a_2'].append(thermo_values1[0])
			data['a_1'].append(thermo_values1[1])
			data['a0'].append(thermo_values1[2])
			data['a1'].append(thermo_values1[3])
			data['a2'].append(thermo_values1[4])
			data['a3'].append(thermo_values1[5])
			data['a4'].append(thermo_values1[6])
			data['a5'].append(thermo_values1[7])
			data['a6'].append(thermo_values1[8])

			data['Temperature range 2'].append(temp_range2)
			data['a_2.2'].append(thermo_values2[0])
			data['a_1.2'].append(thermo_values2[1])
			data['a0.2'].append(thermo_values2[2])
			data['a1.2'].append(thermo_values2[3])
			data['a2.2'].append(thermo_values2[4])
			data['a3.2'].append(thermo_values2[5])
			data['a4.2'].append(thermo_values2[6])
			data['a5.2'].append(thermo_values2[7])
			data['a6.2'].append(thermo_values2[8])

	data = pd.DataFrame(data)
	return data

global base_urltxt
base_url = 'https://rmg.mit.edu/database/thermo/libraries/'


all_files_in_dir = os.listdir()
if 'libraries.txt' not in all_files_in_dir:
	libraries = get_list_libraries()
	fout = open('libraries.txt', 'w')
	for i in libraries:
		fout.write(i + "\n")
	fout.close()	
else:
	libraries = []
	fin = open('libraries.txt')
	libraries = fin.read().splitlines()
	fin.close()

read_flag = False
for lib in libraries:
	if lib == "BurcatNS" or read_flag:
		read_flag = True
		data = get_dataframe(lib)
		if 'data.csv' not in os.listdir():
			data.to_csv('data.csv')
		else:	
			data.to_csv('data.csv', mode='a', header=False)