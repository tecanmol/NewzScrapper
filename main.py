from ScrapLinks import get_headlines
from ScrapData import get_content
from analyze import analyzeContent
from notify import send_notification
import json
url = 'https://news.ycombinator.com/'

print("Fetching headlines...")
newz = get_headlines(url)

all_articles = []

for item in newz:
    print(f"Scraping: {item['title']}...")
    # print(item['link'])
    # Get the body text
    body_text = get_content(item["link"].strip())
    
    # Create a dictionary for this specific article
    article_data = {
        "rank": item["rank"],
        "title": item["title"],
        "link": item["link"],
        "content": body_text if body_text else "No content found"
    }

    all_articles.append(article_data)

final_json_payload = json.dumps(all_articles, indent=2)
print("Analyzing all articles...")
response = analyzeContent(final_json_payload)
raw_text = response.candidates[0].content.parts[0].text
cleaned = raw_text.strip().lstrip("```json").rstrip("```")

summary = json.loads(cleaned)
for item in summary:
    # 1. Check if data is nested inside a 'summary' key or sits at the top level
    data = item.get('summary', item)
    
    # 2. Format the Key Takeaways (which is a list) into a readable string
    takeaways = data.get('Key Takeaways', [])
    if isinstance(takeaways, list):
        formatted_takeaways = "\n      - " + "\n      - ".join(takeaways)
    else:
        formatted_takeaways = takeaways

    # 3. Construct the message safely
    message = f"""
    Title: {item.get('title', 'No Title')}
    TL;DR: {data.get('TL;DR', 'N/A')}
    Key Takeaways: {formatted_takeaways}
    Category: {data.get('Category', 'N/A')}
    Link: {item.get('link', 'No Link Available')}
    """
    
    print(f"sent: {item.get('title', 'Unknown')}")
    send_notification(message)

    

# l ='https://foxmoss.com/blog/dote/'
# get_data(l)
