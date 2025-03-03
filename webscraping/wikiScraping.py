import sys

from bs4 import BeautifulSoup
import requests

choice = input("choose a wikipedia page")

url = "https://en.wikipedia.org/wiki/" + choice

r = requests.get(url)
parser = BeautifulSoup(r.content, 'html.parser')

# this table only exists if the user's choice is not a wikipedia article
notFound = parser.find("table", {"id":"noarticletext"})

# end the program if the table is found
if notFound != None:
    print("this article does not exist")
    sys.exit()

numP = int(input("how many paragraphs do you want to see?"))

# find the first div whose id is bodyContent
container = parser.find("div", {"id":"bodyContent"})

# find all the paragraphs within this div
paragraphs = container.find_all("p")

# if there aren't enough paragraphs 
if len(paragraphs) < numP + 1:
    print("There are not this many paragraphs in the page")
    numP = len(paragraphs) - 1

# print all the paragraphs, skipping the empty first one
for i in range(1, numP+1):
    print(paragraphs[i].text)

