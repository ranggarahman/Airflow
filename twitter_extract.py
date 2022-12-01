import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs


def run_twitter_extract():

    api_key = "c7teHMdEtATuelCefrf9SiUaL"
    api_secret = "XnwICgD1S6xNmYUf7Z0sDy1N65pTd0oOhKgBXQTjy5QitCqKBO"
    access_key = "857121277626155008-s011sarjAg138ZzOcQxMfvgUke3kTVk"
    access_secret = "PrRXFVeuBZVFvMMdSbf0XYYL0Jkz0QOnRMYyw0HlpKjWf"

    # Twitter authentication
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_key, access_secret)

    # Creating an API object
    api = tweepy.API(auth)

    tweets = api.search(q="World Cup",
                        lang="en",
                        count=100,
                        )

    tweet_list = []
    for tweet in tweets:
        refined_tweet = {
            'text': tweet.text,
            # 'created_at': tweet.created_at
        }
        tweet_list.append(refined_tweet)

    df = pd.DataFrame(tweet_list)
    df = df.to_json()
    return df
