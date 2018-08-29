from bs4 import BeautifulSoup
import requests

class TextExtractor:
	def __init__(self, url):
		self.url = url
		self.validUrls = set()
		self.extract()

	def extract(self):
		page = requests.get(self.url)
		bsoup = BeautifulSoup(page.text, 'html.parser')
		self.add_valid_urls_from_page(bsoup)
		for current_url in self.validUrls:
			page = requests.get(current_url)
			bsoup = BeautifulSoup(page.text, 'html.parser')
			self.add_text_from_page(bsoup, current_url)

	def add_text_from_page(self, bsoup, cuurent_url):
		with open('text.txt', 'a') as f:
			#f.write("Current Url - " + str(cuurent_url)+ '\n')
			for chunk in bsoup.find_all('p'):
				f.write(str(chunk.text))
			f.write('\n')

	def is_valid_url(self, check_url):
		return check_url.endswith('.html')

	def add_valid_urls_from_page(self, bsoup):
		counter = 0
		for ahref in bsoup.find_all('a'):
			url = ahref.get('href')
			if url:
				url = url.strip()
				if self.is_valid_url(url):
					self.validUrls.add(url)
					counter += 1
			if counter > 50:
				break

#ext = TextExtractor('https://www.hindustantimes.com/')

def analyse(file_path):
	text = []
	with open(file_path, 'r') as f:
		one_text = []
		for line in f:
			if line.strip():
				one_text.append(line)
			else:
				text.append(one_text)
				one_text =[]

	return text

text = analyse('text.txt')	

from sentiment import Sentiment
sentim = Sentiment(text)
sentim.sentiment_polarity()



'''from selenium import webdriver
import os

options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium-browser"

chromedriver = "/usr/bin/chromedriver"
#os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
#url = input("Enter the url - ")
driver.get("https://en.wikipedia.org/wiki/Artificial_intelligence#Video_games")

element = driver.find_element_by_class('mw-headline')
all_tweets = element.text
print(all_tweets)'''