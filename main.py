import tweepy
from time import sleep
import os

access_token_secret = os.environ['access_token_secret']
access_token = os.environ['access_token']
consumer_secret = os.environ['consumer_secret']
consumer_key = os.environ['consumer_key']
bearer_token = os.environ['bearer_token']

client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

print("Tweet bot online, by bankkroll.eth")

# Open text file for reading
my_file = open('tweets.txt', 'r')

# Read lines one by one and assign to file_lines variable
file_lines = my_file.readlines()

# Close file
my_file.close()

# Tweet a line every 24hrs
def tweet():
    for line in file_lines:
        try:
             print(line)
             if line != '\n':
                 api.update_status(line)
                 sleep(86400)
             else:
                pass
        except tweepy.errors.TweepyException as e:
            print(e)

while True:

    tweet()
