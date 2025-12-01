import requests
from bs4 import BeautifulSoup

def get_content(url):
    response = requests.get(url)
    rawContent = response.text
    # print(rawContent)
    soup = BeautifulSoup(rawContent, 'html.parser')
    
    # print(soup.prettify())

    possible_selectors = [
        "article",
        "main article",
        "main",
        ".prose",
        ".post-content",
        ".content",
        ".article-content",
        ".entry-content",
        "#content",
    ]

    for selector in possible_selectors:
        el = soup.select_one(selector)
        if el:
            return el.get_text(" ", strip=True)

    return "No content found"