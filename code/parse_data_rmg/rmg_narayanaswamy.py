# import urllib.request
import csv
from bs4 import BeautifulSoup as bs

def get_narayanaswamy_webpages():
	fin = open("RMG Thermodynamics Libraries narayanaswamy.html")
	html = fin.read()
	fin.close()
	soup = bs(html, 'lxml')

	tr_lists = soup.find_all("tr")
	tr_lists = tr_lists[1:]

	mappings = {}
	# label_list = []
	link_list = []
	molecule_list = []
	for i,j in enumerate(tr_lists):
		# if i%3 != 2:
		link_list.append(j.find("a").text.split(".")[0])
		molecule_list.append(j.find("a").text.split(".")[1])

	for j,i in zip(molecule_list, link_list):
		mappings[int(i)] = j

	# print(mappings)

	return mappings


if __name__ == "__main__":
	MAPPINGS = get_narayanaswamy_webpages()

	for i in MAPPINGS:
		print(i, MAPPINGS[i])