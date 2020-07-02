import urllib.request
import csv
from bs4 import BeautifulSoup as bs

def rmg_link_lists():
	url = "https://rmg.mit.edu/database/thermo/libraries/"
	html = (urllib.request.urlopen(url)).read()
	soup = bs(html, 'lxml')

	li_lists = soup.find_all("li")
	li_lists = li_lists[4:]

	link_lists = []
	for i in li_lists:
		link_lists.append(i.text.split()[0])

	return link_lists

if __name__ == "__main__":
	LINK_LISTS = rmg_link_lists() 
	# for i in LINK_LISTS:
		# print(i)
	print(LINK_LISTS)