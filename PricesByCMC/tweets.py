"""
@author : GaloisField
"""

import messages
import tweepy
import config
from urllib import response

# Tweepy client initialisation.
# Initialisation du client Tweepy.
client = tweepy.Client(consumer_key=config.API_KEY, consumer_secret=config.API_KEY_SECRET, access_token=config.ACCESS_TOKEN, access_token_secret=config.ACCESS_TOKEN_SECRET)


# Create the first tweet with price informations.
# Crée le premier tweet avec les informations des cours.
response1 = client.create_tweet(text=message.message1)
print(f"https://twitter.com/user/status/{response1.data['id']}\n")

# Create an answer to first tweet with the volumes.
# Crée une réponse au premier tweet avec les volumes.
response2 = client.create_tweet(in_reply_to_tweet_id=response1.data['id'], text=message.message2)
print(f"https://twitter.com/user/status/{response2.data['id']}\n")

# Comment with Hashtags.
# Commente avec les Hashtags.
response3 = client.create_tweet(in_reply_to_tweet_id=response2.data['id'], text=message.message3)
print(f"https://twitter.com/user/status/{response3.data['id']}")

