# twitter_trends.py

import tweepy

def get_twitter_trends(api_key, api_secret_key, access_token, access_token_secret, woeid=23424829):
    auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
    api = tweepy.API(auth)
    trends = api.get_place_trends(woeid)
    trend_names = [trend['name'] for trend in trends[0]['trends']]
    return trend_names