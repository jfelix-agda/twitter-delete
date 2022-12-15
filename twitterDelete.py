# This program deletes all tweets up until 1 year ago from today.
# Created by: John Felix Agda

from datetime import datetime, timedelta
from xml.etree.ElementTree import tostring
import tweepy
import configparser
import time
import os

# Reads config.ini
config = configparser.RawConfigParser()
config.read('config.ini')

conffile = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.ini')
config.read(conffile)

apiKey = config['twitterInfo']['apiKey']
apiKeySecret = config['twitterInfo']['apiKeySecret']
bearerToken = config['twitterInfo']['bearerToken']

accessToken = config['twitterInfo']['accessToken']
accessTokenSecret = config['twitterInfo']['accessTokenSecret']

# Contains my personal user ID
userID = config['twitterInfo']['userID']

# Authentication
client = tweepy.Client(
    consumer_key= apiKey,
    consumer_secret= apiKeySecret,
    access_token= accessToken,
    access_token_secret= accessTokenSecret,
    bearer_token=bearerToken
)

# Calculates the date 1 year ago from today
currentDate = datetime.today()
minDate = datetime.today() - timedelta(days=365)

# Queries the list of tweets
tweetPaginator = tweepy.Paginator(client.get_users_tweets,userID,max_results=100,start_time=minDate, end_time=currentDate)

# Deletes the tweets
for tweet in tweetPaginator.flatten():
    print("Deleting Tweet:")
    print(tweet.id)
    client.delete_tweet(tweet.id)
    time.sleep(0.5)


