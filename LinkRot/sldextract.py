def extract(url):
	f = open("tld.txt", 'r')

	tld_list = (f.read()).split(",\n  ")

	for i in tld_list:
		if i in url:
			url_tld = i

	url.remove(url_tld)
	url.remove("https://")
	url = url[:url.index('/')]
	url_domain = url.strip('.')
	return url_domain




