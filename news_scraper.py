# news_scraper.py

import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')

        # Try to find headlines in <h2> or <h3> or <a> tags with specific classes
        # This is customizable depending on the site structure
        headlines = []

        for tag in soup.find_all(['h1', 'h2', 'h3']):
            text = tag.get_text(strip=True)
            if text and len(text) > 15:  # Filter short/irrelevant text
                headlines.append(text)

        return headlines

    except requests.RequestException as e:
        print(f"Error fetching news: {e}")
        return []

def save_headlines(headlines, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for line in headlines:
            file.write(line + '\n')

def main():
    url = "https://www.bbc.com/news"  # Example news site
    headlines = fetch_headlines(url)
    if headlines:
        print(f"Fetched {len(headlines)} headlines.")
        save_headlines(headlines, "headlines.txt")
        print("Headlines saved to headlines.txt")
    else:
        print("No headlines found or failed to fetch.")

if __name__ == "__main__":
    main()
