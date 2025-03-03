import sys

from bs4 import BeautifulSoup
import requests

choice = input("choose a wikipedia page")

url = "https://en.wikipedia.org/wiki/" + choice

r = requests.get(url)
parser = BeautifulSoup(r.content, 'html.parser')

notFound = parser.find("table", {"id":"noarticletext"})

if notFound != None:
    print("this article does not exist")
    sys.exit()

numP = int(input("how many paragraphs do you want to see?"))

container = parser.find("div", {"id":"bodyContent"})

paragraphs = container.find_all("p")

# if there aren't enough paragraphs
if len(paragraphs) < numP + 1:
    print("There are not this many paragraphs in the page")
    numP = len(paragraphs) - 1

for i in range(1, numP+1):
    print(paragraphs[i].text)

