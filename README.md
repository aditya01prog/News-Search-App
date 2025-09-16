# News Search App

A Python script that allows users to search for news articles on any topic using the NewsAPI. It fetches popular news articles from a specified date and displays their titles and URLs in the terminal.

## Features
- Search for news on any topic.
- Displays article titles and links.
- Uses NewsAPI for real-time news data.
- Simple and interactive input.

## Requirements
- Python 3.x
- `requests` library
- A NewsAPI API key (https://newsapi.org)

Install the required library using:
    pip install requests

## How to use
1. Get a free API key from [NewsAPI](https://newsapi.org).
2. Replace the `api` variable in the script with your API key.
3. Run the script using:
    python news_search.py
4. Enter the topic you want to search for when prompted.
5. The script will display popular news articles with titles and URLs.

## Notes
- The date range is currently fixed in the script. You can modify the 'from' and 'to' parameters in the URL to search for different dates.
- Ensure your API key is kept secure and not shared publicly.

## Disclaimer
This is a learning project. For extensive use or production-level applications, follow NewsAPI’s terms and conditions.

---

Stay informed with the latest news!
