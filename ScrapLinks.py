import json
import requests
from bs4 import BeautifulSoup

def get_headlines(url):

    response = requests.get(url)
    content = response.text

    soup = BeautifulSoup(content, 'html.parser')

    headlines = []
    for item in soup.select("span.titleline a"):
        row = item.find_parent("tr")
        rank_tag = row.select_one("span.rank")
        rank = int(rank_tag.get_text(strip=True).replace(".",""))
        title = item.get_text(strip=True)
        link = item["href"].strip()
        if not link.startswith("http"):
            print(f"Skipping invalid link: {link}")
            continue
        headlines.append({"rank": rank, "title": title, "link": link})

        if rank == 10:
            break
        # print(headlines)
    return headlines

