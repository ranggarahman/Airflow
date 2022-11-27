from tweepy import API 
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import pandas as pd
import json
from datetime import datetime
import s3fs
from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings

def run_twitter_etl():
  # For twitter API credentials
  class Credentials():
    def __init__(self, access_token, access_token_secret, consumer_key, consumer_secret):
      self.ACCESS_TOKEN = access_token
      self.ACCESS_TOKEN_SECRET = access_token_secret
      self.CONSUMER_KEY = consumer_key
      self.CONSUMER_SECRET = consumer_secret
  ACCESS_TOKEN = "1153291455340765184-AH0fD3WMlIOmdChkVMmAtWV18zD8OE"
  ACCESS_TOKEN_SECRET = "b8QtThweLDp0hGEiawIqRxFZAtCKILpCh3keWcft56AO4"
  CONSUMER_KEY = "i9UvhwXbvVxWCI6ymXb6gUuSv"
  CONSUMER_SECRET = "fRAzewVdYvjDt2edPh8EhCZMVBniTMKCtNaSqpELa9Ka63IQr8"
  twitter_credentials = Credentials(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

  #To Authenticate the access to twitter API
  class TwitterAuthenticator():
      def authenticate_twitter_app(self):
          auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
          auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
          return auth

  class TwitterClient():
      def __init__(self, twitter_user=None):
          self.auth = TwitterAuthenticator().authenticate_twitter_app()
          self.twitter_client = API(self.auth)

          self.twitter_user = twitter_user
      def get_twitter_client_api(self):
        return self.twitter_client

  class TweetAnalyzer():
    def tweets_to_data_frame(self, tweets):
      tweet_list = []
      for tweet in tweets:
        refined_tweet = {
                          # "user" : tweet.user.screen_name,
                          "text" : tweet.text,
                          "created_at" : tweet.created_at}
        tweet_list.append(refined_tweet)

      df = pd.DataFrame(tweet_list)
      return df

  tweet_analyzer = TweetAnalyzer()
  twitter_client = TwitterClient()
  api = twitter_client.get_twitter_client_api()

  tweets = api.search(q = "\"World Cup\" lang:en -filter:links", count=100)
  df_tate = tweet_analyzer.tweets_to_data_frame(tweets)

  df_tate.to_csv('world_cup_tweet.csv')

  block_blob_service = BlockBlobService(account_name='azurewonderful',account_key='JRyejoZn/9Qzg7UMWswAm+EM+prmVQDqzikwGUA1xEuGFPdiN9fJDAbvFZBuP2UfzJWub3bACs4I+AStYIdK/w==')
  # block_blob_service.create_container('mycontainer')

  #Upload the CSV file to Azure cloud
  block_blob_service.create_blob_from_path(
      'mycontainer',
      'myblockblob.csv',
      'world_cup_tweet.csv',
      content_settings=ContentSettings(content_type='application/CSV')
      )

  # # Check the list of blob
  # generator = block_blob_service.list_blobs('mycontainer')
  # for blob in generator:
  #     print(blob.name)