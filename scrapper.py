from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

# Scrape Function
def scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    posts = []
    titles = soup.find_all("h3", attrs={"class": "contentRow-title"})

    for title in titles:
        link = title.find("a") 
        if link:
            posts.append({
                "title": title.get_text(strip=True),
                "url": urljoin(url, str(link["href"]))
            })      
    return posts







