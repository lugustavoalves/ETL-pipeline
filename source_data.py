import os
import time
from newsapi import NewsApiClient
import json

key = "XXXXXXXXXX"
# Initialize API endpoint
newsapi = NewsApiClient(api_key=key)

# Define the list of media sources
sources = 'bbc-news,cnn,fox-news,nbc-news,the-guardian-uk,the-new-york-times,the-washington-post,usa-today,independent,daily-mail'

all_articles = newsapi.get_everything(q='bitcoin OR cryptocurrency OR crypto OR BTC OR btc',
                                      sources=sources,
                                      language='en')

# using a loop to simulate stream data
for article in all_articles['articles']:
    # check if the file exists
    if os.path.exists('articles.json'):
        # read the existing content
        with open('articles.json', 'r') as f:
            articles = json.load(f)
    else:
        articles = []

    if article not in articles: # make sure no duplicate
        articles.append(article)
        print(f"processing article: {article['title']}")
        # save the updated list back to the file
        with open('articles.json', 'w') as f:
            json.dump(articles, f, indent=4) # indent=4 is for better readability
        time.sleep(1) # to simulate stream data
    else:
        pass
