from bs4 import BeautifulSoup
import requests


# lets the user enter a name, then finds that player's receiving yards for 2024 season
def wrSearch():

    choice = input("choose a wide receiver: ").strip()

    url = "https://www.nfl.com/stats/player-stats/category/receiving/2024/reg/all/receivingreceptions/desc"

    r = requests.get(url)
    parser = BeautifulSoup(r.content, "html.parser")

    table = parser.find("tbody")
    rows = table.find_all("tr")

    for r in rows:
        name = r.find("td").text.strip()
        if name.lower() == choice.lower():
            print(name, "had", r.find_all("td")[2].text.strip())







# crawls through every receiver's player page to find their height, then computes the average
def avgHeight():

    url = "https://www.nfl.com/stats/player-stats/category/receiving/2024/reg/all/receivingreceptions/desc"

    r = requests.get(url)
    parser = BeautifulSoup(r.content, "html.parser")

    table = parser.find("tbody")

    rows = table.find_all("tr")

    total = 0

    for r in rows:

        link = "https://www.nfl.com" + r.find("a")["href"]

        r = requests.get(link)
        playerPage = BeautifulSoup(r.content, "html.parser")

        infoSection = playerPage.find("div", {"class":"d3-l-col__col-12 nfl-c-player-info__content"})

        height = infoSection.find("div", {"class":"nfl-c-player-info__value"}).text.strip()

        heightNum = int(height.split("-")[0]) * 12 + int(height.split("-")[1])

        total += heightNum

    print("The average height of nfl receivers is", total/len(rows), "in")





wrSearch()