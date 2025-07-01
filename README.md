# Web-Scraper-for-News-Headlines

# News Headline Scraper
## Overview
This Python script fetches the top news headlines from a news website using web scraping.

## How It Works
- Uses `requests` to fetch the HTML content from the website.
- Uses `BeautifulSoup` to parse the HTML and extract news headlines from `<h1>`, `<h2>`, and `<h3>` tags.
- Saves the extracted headlines to a file named `headlines.txt`.

## Requirements
- `requests`
- `beautifulsoup4`

Install them with:
```bash
pip install requests beautifulsoup4
```

## How to Run
```bash
python news_scraper.py
```

## Output
- `headlines.txt` — contains the scraped news headlines.

## Note
This script uses `https://www.bbc.com/news` as an example. You can change the URL based on your preferred news website (make sure it's allowed for scraping).
