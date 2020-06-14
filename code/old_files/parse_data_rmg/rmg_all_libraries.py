import urllib
import csv
from bs4 import BeautifulSoup as bs
from rmg_parser import rmg_link_lists

def get_library_webpages(lib):
	url = f"https://rmg.mit.edu/database/thermo/libraries/{lib}/"
	html = (urllib.request.urlopen(url)).read()
	soup = bs(html, 'lxml')

	tr_lists = soup.find_all("tr")
	tr_lists = tr_lists[1:]

	mappings = {}
	# label_list = []
	link_list = []
	molecule_list = []
	for i,j in enumerate(tr_lists):
		if j.find_all("td")[-1].text == "NASA":
			link_list.append(j.find("a").text.split(".")[0])
			molecule_list.append(j.find("a").text.split(".")[1])

	for j,i in zip(molecule_list, link_list):
		mappings[int(i)] = j

	# print(mappings)

	return mappings


if __name__ == "__main__":
	link_lists = rmg_link_lists()
	for i in link_lists:
		MAPPINGS = get_library_webpages(i)
		if i == "Narayanaswamy":
			for i in MAPPINGS:
				print(i, MAPPINGS[i])