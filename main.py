import requests
query = input("On what topic would you like to search a news ? ") 
api = "your_api_key"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-08-06&to=2025-08-06&sortBy=popularity&apiKey={api}"

print(url)

r = requests.get(url)
data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index+1, article["title"])
    print(article["url"])

    print("\n*************************************\n")
