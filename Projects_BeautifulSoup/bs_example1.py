#Example from 
#https://towardsdatascience.com/introduction-to-web-scraping-with-beautifulsoup-e87a06c2b857
#import libraries
import sys
sys.path.append("")
#from bs4 import BeautifulSoup #package used for webscraping

import urlib.request 
# for connecting to HTML

import re #package for reqular expressions

url ="https://en.wikipedia.org/wiki/Artificial_intelligence" # we are webscraping this url

page=urlib.request.urlopen(url) #Connect to website

#We are using try-catch to open the url to be web scraped

try:
	page=urlib.request.urlopen(url)
except:
	print("An error occurred")	

soup=BeautifulSoup(page,'html.parser')
print(soup)
regex=re.compile('^tocsection-')
content_lis=soup.find_all('li',attrs={'class':regex})
print(content-lis)