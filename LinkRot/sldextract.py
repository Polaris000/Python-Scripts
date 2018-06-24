def extract(url):
	f = open("tld.txt", 'r')

	tld_list = (f.read()).split(",\n  ")

	# print(tld_list)
	url = url.replace("https://", "")
	if '/' in url:
		url = url[:url.index('/')]
	# print(url)

	for i in tld_list:
		if url.endswith(i):
			url_tld = i

			url = url.replace(url_tld, "")
			# print(i)
			break

	else:
		url_tld = ""


	# print(url)
	
	
	# print(url)
	
	

	# print(url)
	url_domain = url.strip('.')
	# print(url)


	url_contents = {"url_domain": url_domain, "url_tld": url_tld}
	return url_contents




