# trends.py

from pytrends.request import TrendReq

def get_google_trends(keyword, timeframe='now 7-d'):
    pytrends = TrendReq(hl='de-DE', tz=360)
    pytrends.build_payload([keyword], cat=0, timeframe=timeframe, geo='', gprop='')
    data = pytrends.related_queries()
    top_queries = data[keyword]['top']
    if top_queries is not None:
        return top_queries['query'].tolist()
    else:
        return []