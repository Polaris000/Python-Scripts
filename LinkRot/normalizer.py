def normalize(url, main_url_domain):
	if url[0] == "#":

		url = "https://" + str(main_url_domain) + "/" + url

	elif url.startswith('//'):
		url = "https:" + url

	elif url.startswith("mailto:"):
		url = None

	return url