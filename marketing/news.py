# news.py

from newsapi import NewsApiClient

def get_top_headlines(api_key, language='de', page_size=10):
    newsapi = NewsApiClient(api_key=api_key)
    headlines = newsapi.get_top_headlines(language=language, page_size=page_size)
    articles = headlines['articles']
    titles = [article['title'] for article in articles]
    return titles