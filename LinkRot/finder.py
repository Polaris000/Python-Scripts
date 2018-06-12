import requests
from bs4 import BeautifulSoup
import tldextract as t
import sys


broken_links = []
checked_links = []
count = 0

checked_file = open("checked_urls.csv", "w")
broken_file = open("broken_urls.csv", "w")

checked_file.write("Sr_No." + "," + "url" + "," + "status_code" + "," + "Proper" + "\n")
broken_file.write("url" + "," + "status_code" + "\n")

def read_url(url):
	# url = "https://www.craigslist.org/about/sites"
	global count

	url_request = requests.get(url)

	count += 1
	print(count)
	url_domain = t.extract(url).domain

	is_ok = True

	if url_request.status_code >= 400:

		broken_links.append(url)
		is_ok = False
		broken_file.write(url + "," + str(url_request.status_code) + "\n")


	print(url_request.status_code)
	soup = BeautifulSoup(url_request.content, "html.parser")

	url_list = soup.find_all('a', href=True)
	checked_links.append(url)

	checked_file.write(str(count) + "," + url + "," + str(url_request.status_code) + "," + str(is_ok) + "\n")

	for link in url_list:

		new_url = t.extract(link['href'])

		if new_url.domain == url_domain and link['href'] not in checked_links:
			print(link['href'])
			read_url(link['href'])

	else:
		pass


if __name__ == '__main__':
	url = sys.argv[1]

	read_url(url)
	checked_file.close()
	broken_file.close()
