import requests
from bs4 import BeautifulSoup

url = 'https://toscrape.com/'


def linkSaver(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

def elementsSaver(links):
    for link in links:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')
        h1 = soup.find_all("h1")
        p = soup.find_all("p")
        print("Link: ", link)
        print("H1 tags: ", h1)
        print("P tags: ", p)

links = linkSaver(url)
elementsSaver(links)