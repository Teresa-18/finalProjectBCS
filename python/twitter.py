
# pip install tweepy
from config import consumer_key,consumer_secret,access_token,access_token_secret
import tweepy
from tweepy import API 
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime as dt
import numpy as np
import pandas as pd

# Output Files (CSV)
output_data_file = "./output_data/monday_tweets.csv"
output_data_file2 = "./output_data/friday_tweets.csv"
output_data_file3 = "./output_data/spring_tweets.csv"

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

#03/07/2021
date_since = (dt.datetime(2021, 3, 7)).strftime("%Y-%m-%d")
#03/09/2021
date_until = (dt.datetime(2021, 3, 9)).strftime("%Y-%m-%d")

#03/11/2021
date_since2 = (dt.datetime(2021, 3, 11)).strftime("%Y-%m-%d")
#03/13/2021
date_until2 = (dt.datetime(2021, 3, 13)).strftime("%Y-%m-%d")

#03/19/2021
date_since3 = (dt.datetime(2021, 3, 19)).strftime("%Y-%m-%d")
#03/21/2021
date_until3 = (dt.datetime(2021, 3, 21)).strftime("%Y-%m-%d")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication Complete")
except:
    print("Authentication Unable to Complete")

mondaytweets = []
for tweet in tweepy.Cursor(api.search, q='monday', lang='en', rpp=100, since=date_since, until=date_until).items(450):
    mondaytweets.append(tweet)
# print(mondaytweets)

fridaytweets = []
for tweet in tweepy.Cursor(api.search, q='monday', lang='en', rpp=100, since=date_since2, until=date_until2).items(450):
    mondaytweets.append(tweet)
# print(mondaytweets) 

springtweets = []
for tweet in tweepy.Cursor(api.search, q='monday', lang='en', rpp=100, since=date_since3, until=date_until3).items(450):
    mondaytweets.append(tweet)
# print(mondaytweets)   

class TweetAnalyzer():
    def tweets_to_data_frame(self, mondaytweets):
            df = pd.DataFrame(data=[mondaytweets.text for tweet in mondaytweets], columns=['monday_tweets'])
    
            # df['id'] = np.array([tweet.id for tweet in tweets])
            # df['len'] = np.array([len(tweet.text) for tweet in tweets])
            # df['date'] = np.array([tweet.created_at for tweet in tweets])
            # df['source'] = np.array([tweet.source for tweet in tweets])
            # df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
            # df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
    
            return df

class TweetAnalyzer2():
    def tweets_to_data_frame(self, fridaytweets):
            df2 = pd.DataFrame(data=[fridaytweets.text for tweet in fridaytweets], columns=['friday_tweets'])
    
            # df['id'] = np.array([tweet.id for tweet in tweets])
            # df['len'] = np.array([len(tweet.text) for tweet in tweets])
            # df['date'] = np.array([tweet.created_at for tweet in tweets])
            # df['source'] = np.array([tweet.source for tweet in tweets])
            # df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
            # df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
    
            return df2

class TweetAnalyzer3():
    def tweets_to_data_frame(self, springtweets):
            df3 = pd.DataFrame(data=[springtweets.text for tweet in springtweets], columns=['spring_tweets'])
    
            # df['id'] = np.array([tweet.id for tweet in tweets])
            # df['len'] = np.array([len(tweet.text) for tweet in tweets])
            # df['date'] = np.array([tweet.created_at for tweet in tweets])
            # df['source'] = np.array([tweet.source for tweet in tweets])
            # df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
            # df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
    
            return df3

if __name__ == '__main__':

    tweet_analyzer = TweetAnalyzer()
    df = tweet_analyzer.tweets_to_data_frame(mondaytweets)
    print(df.head(10))
    df.to_csv(output_data_file)

    tweet_analyzer = TweetAnalyzer2()
    df2 = tweet_analyzer.tweets_to_data_frame(fridaytweets)
    print(df2.head(10))
    df.to_csv(output_data_file2)


    tweet_analyzer = TweetAnalyzer3()
    df3 = tweet_analyzer.tweets_to_data_frame(springtweets)
    print(df3.head(10))
    df.to_csv(output_data_file3)



# #Write DataFrame to CSV file "tweets.csv"
# df.to_csv(output_data_file)
