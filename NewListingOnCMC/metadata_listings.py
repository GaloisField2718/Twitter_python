from listings_cmc import *
import tweets_wrapper

########################################################################################
################	FUNCTIONS TO TREAT METADATA 					####################
########################################################################################

"""
@note : Je n'arrive pas à mettre deux ids dans les paramètres.
		Du coup, je fais une fonction que j'appelerais.
		Néanmoins, chaque appel de la fonction est un appel à l'API.
"""
def getTextMetadata_from_cmc_id(_id): 

	"""
		Open connexion with CMC
	"""
	headers = {
		'Accepts' : 'application/json',
		'X-CMC_PRO_API_KEY' : 'cbcd926b-75e5-48be-b736-106d81489cf4'
	}

	session = Session()
	session.headers.update(headers)

	"""
		@param : _id
	"""
	urlMetadata = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info'

	parametersMetadata = {
		'id' : _id
	}
	
	"""
		@note : get Metadata by call API
	"""
	responseMetadata = session.get(urlMetadata, params=parametersMetadata)
	
	"""
		@note : formats data to use as text
	"""
	textMetadata = json.loads(responseMetadata.text)['data'][f'{_id}']


	return textMetadata

def messageVariableEmpty(list,symbol_empty, message):
	if list == symbol_empty:
		list = message
	return list


"""
	@constants
"""

max_length = 200

########################################################################################
#################		GET LAST LISTED METADATA's TOKEN				################
########################################################################################

metadata_lastListing = getTextMetadata_from_cmc_id(id_lastListing)
metadata_previousListing = getTextMetadata_from_cmc_id(id_previousListing)

description_lastListing = "⿶ Description : " + metadata_lastListing['description']
description_previousListing = "⿻ Description : " + metadata_previousListing['description']

"""
	@part : description

	@note : create blocks of 240 characters to be allowed to add 
	some characters at the begin and the end of the final tweets.
"""

blocks_descr_lListing = tweets_wrapper.tweets_wrapper(description_lastListing, max_length)
blocks_descr_pListing = tweets_wrapper.tweets_wrapper(description_previousListing, max_length)

""" 
	@part : Twitter username
"""

twitter_username_lListing = metadata_lastListing['twitter_username']
twitter_username_pListing = metadata_previousListing['twitter_username']

"""
	@part : subreddit
"""
message_noSubreddit = "NO SUBREDDIT PROVIDED FOR CMC"
empty_symbol_sub = ''
subreddit_lListing = messageVariableEmpty(metadata_lastListing['subreddit'], empty_symbol_sub, message_noSubreddit)
subreddit_pListing = messageVariableEmpty(metadata_previousListing['subreddit'], empty_symbol_sub, message_noSubreddit)

message_noReddit = "NO REDDIT !"
empty_symbol_reddit = []
reddit_lListing = messageVariableEmpty(metadata_lastListing['urls']['reddit'], empty_symbol_reddit, message_noReddit)
reddit_pListing = messageVariableEmpty(metadata_previousListing['urls']['reddit'], empty_symbol_reddit, message_noReddit)

"""
	@part : website
"""
message_noWebsite = "⚠️⛔️  NO WEBSITE WAS PROVIDED !!!!!!!!!!!  ☣️⚠️"
empty_symbol_website = []
website_lListing = messageVariableEmpty(metadata_lastListing['urls']['website'], empty_symbol_website, message_noWebsite)
website_pListing = messageVariableEmpty(metadata_previousListing['urls']['website'], empty_symbol_website, message_noWebsite)


"""
	@part : source code 
"""
message_noSourceCode = "⚠️  NO SOURCE WAS PROVIDED !! ⚠️"
empty_symbol_code = []
source_code_lListing = messageVariableEmpty(metadata_lastListing['urls']['source_code'], empty_symbol_code, message_noSourceCode)
source_code_pListing = messageVariableEmpty(metadata_previousListing['urls']['source_code'], empty_symbol_code, message_noSourceCode)



"""
	@part : group urls in blocks
"""

urls_lListing = f" 🌐 MAIN URLs LINK 👉 \n \n Reddit : {reddit_lListing} \n Subreddit : {subreddit_lListing} \n Source code : {source_code_lListing} \n Website : {website_lListing}"
blocks_urls_lListing = tweets_wrapper.tweets_wrapper(urls_lListing, max_length)

urls_pListing = f" 🌐 MAIN URLs LINK 👉 \n \n Reddit : {reddit_pListing} \n Subreddit : {subreddit_pListing} \n Source code : {source_code_pListing} \n Website : {website_pListing}"
blocks_urls_pListing = tweets_wrapper.tweets_wrapper(urls_pListing, max_length)



####################### 		 TEST 										#####################################################
# print("\n \n ------- TEST FONCTION isVariableEmpty ----------------- \n \n")
# print("DOIT SORTIR ⚠️ NO SOURCE CODE WAS PROVIDED ⚠️ \n \n")
# print(source_code_lListing)



# print("\n \n")
# print(source_code_lListing)
# print("\n \n")
# print(source_code_pListing)
# print("\n \n")
# print(reddit_lListing)
# print("\n \n")
# print(reddit_pListing)
# print("\n \n")
# print(subreddit_lListing)
# print("\n \n")
# print(subreddit_pListing)
# print("\n \n")
# print(website_lListing)
# print("\n \n")
# print(website_pListing)


# print('\n \n \n')
# print(blocks_urls_lListing[0])
# print('\n \n \n')
# print(blocks_urls_pListing[0])
# print('\n \n \n')









#################################################################################################################################

