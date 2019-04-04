# Scraping with Beautiful Soup

from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com" # uniform resource locator

page = requests.get(url)
print(page)
#print(page.text)

soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify())

# find data in my soup object
# by tagname

title = soup.findAll("title") # returns a list of all tags <title>
print(title)

# by attribute
fontsize = soup.findAll(style="font-size: 8px")
print(fontsize)
for fonts in fontsize:
    print(fonts.text)

# by css class
quotes = soup.findAll(class_="quote")
print(quotes)

for quote in quotes:
    print(quote.txt)

# by strings
einstein = soup.findAll(string="Albert Einstein")

print(einstein)
for e in einstein:
    print(e)

print("\n" * 10)


# combine any of the above
quotes = soup.findAll("span", class_="text")

for quote in quotes:
    print(quote.text.strip())

# find all authors
authors = soup.findAll("small", class_="author", itemprop="author")

for author in authors:
    print(author.next_element)

print(len(quotes), len(authors))

for i in range(len(quotes)):
    print(quotes[i].text)
    print("\t-", authors[i].text)

# target this ----> <a href="/author/Marilyn-Monroe">(about)</a>

# BELOW IS SOME CODE I WROTE FOR DYNAMIC WEBSITE SCRAPING
# I also added code to download pictures from Instagram

#launch url
url = "https://instagram.com/instagram"

from selenium import webdrive

#create a new chrome session
# need to have chromedriver executable in project for this
driver = webdriver.Chrome("data/chromedriver")
driver.implicitly_wait(15) # wait 15 sec to load
driver.get(url)

#Get scroll height
last_heigh = driver.execute_script("returndocument.body.scrollHeight")
