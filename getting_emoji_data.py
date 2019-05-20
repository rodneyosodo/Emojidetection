from bs4 import BeautifulSoup
import requests
import urllib.request

import os
os.chdir("Data")

url = "https://emojipedia.org/apple/"

def finding_url(url):
	response = requests.get(url)
	if response.status_code != 200:
		raise Exception("Response code was: {}".format(response.status_code))
	else:
		soup = BeautifulSoup(response.text, "html.parser")
		image_links = []
		for link in soup.find_all("img"):
			image_links.append(link.get('data-src'))
		return image_links

def main():
	images = finding_url(url)
	counter = 0
	for image in images:
		if image:
			image_url = "{}".format(image)
			splitted_url = image_url.split("/")
			image_name = splitted_url[-1]
			urllib.request.urlretrieve(image_url, image_name)
			if counter % 100 == 0:
				print(counter)
			counter = counter + 1
		else:
			pass
if __name__ == '__main__':
	print("Starting...")
	main()