from metadata_listings import *
import tweepy
import config

"""
	@function : mise en forme tweet
	@param : thread
"""
def fillTweetNumber(thread) : 
	length_thread = len(thread)
	for index in range(length_thread):
		thread[index] = f"{index}/{length_thread} 👉 {thread[index]} ↩️"
	return thread

def postThread(thread):
	fillTweetNumber(thread)
	length_thread = len(thread)
	for index in range(length_thread):
		if index == 0:
			response0 = client.create_tweet(text=thread[index])
		else : 
			response1 = client.create_tweet(in_reply_to_tweet_id= response0.data['id'], text=thread[index])
			response0 = response1
	print(f" All tweets are posted. \n Last tweet is : https://twitter.com/user/status/{response1.data['id']}\n")


thread1 = []
thread2 = []

"""
	@part : Fill Thread 1
"""

message1 = f" ⏰ Last listing on #Coinmarketcap is {name_lastListing}, ${symbol_lastListing}, at {dateAdded_lastListing} \n 👇👇👇👇 More info 👇👇👇👇👇"
message2 = f" 🔗 {chain_lastListing} chain with address : {contractAddress_lastListing}. \n 💰 {priceUSD_lastListing}, for a ranking {rank_lastListing}-th."


thread1.append(message1)
thread1.append(message2)
thread1.append(blocks_descr_lListing)
thread1.append(blocks_urls_lListing)

"""
	@part : Fill Thread 2
"""

message3 = f" 📆 Previous listing on @coinmarketcap was {name_previousListing}, ${symbol_previousListing}, at {dateAdded_previousListing} \n 👇👇👇👇 More info 👇👇👇👇👇"
message4 = f" 🔗 {chain_previousListing} chain with address : {contractAddress_previousListing}. \n 💰 {priceUSD_previousListing}, for a ranking {rank_previousListing}-th."

thread2.append(message3)
thread2.append(message4)
thread2.append(blocks_descr_pListing)
thread2.append(blocks_urls_pListing)


"""
	@part : connexion to tweepy client & postThread call
"""
client = tweepy.Client(consumer_key=config.API_KEY, consumer_secret=config.API_KEY_SECRET, access_token=config.ACCESS_TOKEN, access_token_secret=config.ACCESS_TOKEN_SECRET)


postThread(thread1)
postThread(thread2)



