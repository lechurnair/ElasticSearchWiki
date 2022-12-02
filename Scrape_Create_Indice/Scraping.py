import requests
from bs4 import BeautifulSoup
import json 
# Make a request to the website
r = requests.get('https://en.wikipedia.org/wiki/Science_fiction_film')

# Create an object to parse the HTML format
soup = BeautifulSoup(r.content, 'html.parser')

#this code makes a list of all links in a wiki page

allLinks = soup.find(id="bodyContent").find_all("a")

linkToScrape = []

#checking for links with href containing wiki in it
for link in allLinks:

  if link.get('href') is not None:
    if link['href'].find("/wiki/") == 0: 
      linkToScrape.append("https://en.wikipedia.org"+link['href'])

# print("all links that contain /wiki/ \n")
# print(linkToScrape)
# print(len(linkToScrape))

data_list = []

for ls in linkToScrape:

  data = {}
  data['link'] = ls

  # print(ls)
  page = requests.get(ls)
  soup1 = BeautifulSoup(page.content, 'html.parser')

  data['title'] = soup1.select('h1')[0].text
  print(data['title'])

  data['subheadings'] = []

  for element in soup1.select('h2'):
    data['subheadings'].append(element.text)
  
  data['content'] = ""

  for p in soup1.select('p'):
    data['content'] += p.text
  
  # print(data['content'])

  data_list.append(data)
  
  # with open("sample.json", "a") as outfile:
  #   json.dump(data, outfile)

# now we have a list of dictionaries
# to do - dump into .json

with open("sample.json", "w") as outfile:
  json.dump(data_list, outfile)
