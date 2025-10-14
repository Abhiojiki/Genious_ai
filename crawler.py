"""
crawler.py
Web scraping logic placeholder
"""
from serpapi import GoogleSearch
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Create output folder if it doesn't exist
os.makedirs('output', exist_ok=True)

params = {
    "api_key": os.getenv("SERPAPI_API_KEY"),
    "engine": "google",
    "google_domain": "google.co.in",
    "q": "AI startups 2025",  # Change this to your topic
    "hl": "en",
    "gl": "us",
    "location": "Nagpur, Maharashtra, India",
    "num": "10"
}

all_urls = []

# Get 15 URLs (we'll do 2 pages of 10 results)
for start in range(0, 20, 10):
    params['start'] = str(start)
    search = GoogleSearch(params)
    results = search.get_dict()
    
    org_results = results.get("organic_results", [])
    
    for result in org_results:
        url = result.get('link')
        title = result.get('title')
        if url:
            all_urls.append({'url': url, 'title': title})
            print(f"Found: {title}")
    
    if len(all_urls) >= 15:
        break

# Keep only 15 URLs
all_urls = all_urls[:15]

# Save URLs to output folder
with open("output/urls.json", "w") as f:
    json.dump(all_urls, f, indent=2)

print(f"\nTotal URLs collected: {len(all_urls)}")
print("Saved to output/urls.json")