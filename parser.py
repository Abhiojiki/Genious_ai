import json
import requests
from bs4 import BeautifulSoup
import time
import os

# Create output folder if it doesn't exist
os.makedirs('output', exist_ok=True)

# Load URLs from previous step
with open("output/urls.json", "r") as f:
    urls_data = json.load(f)

all_articles = []

for idx, item in enumerate(urls_data):
    url = item['url']
    print(f"\n[{idx+1}/15] Crawling: {url}")
    
    try:
        # Get webpage content
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract headline
        headline = item['title']
        if not headline:
            h1 = soup.find('h1')
            headline = h1.get_text().strip() if h1 else "No headline"
        
        # Extract main content (paragraphs)
        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text().strip() for p in paragraphs[:10]])  # First 10 paragraphs
        
        # Clean content (remove extra spaces)
        content = ' '.join(content.split())
        
        # Limit content to 2000 characters
        if len(content) > 2000:
            content = content[:2000] + "..."
        
        article = {
            'url': url,
            'headline': headline,
            'content': content
        }
        
        all_articles.append(article)
        print(f"✓ Success: {len(content)} characters extracted")
        
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        # Add empty article so we still have 15 entries
        all_articles.append({
            'url': url,
            'headline': item['title'],
            'content': "Could not extract content"
        })
    
    time.sleep(1)  # Be nice to servers

# Save articles to output folder
with open("output/articles.json", "w", encoding='utf-8') as f:
    json.dump(all_articles, f, indent=2, ensure_ascii=False)

print(f"\n✓ Total articles saved: {len(all_articles)}")
print("Saved to output/articles.json")
