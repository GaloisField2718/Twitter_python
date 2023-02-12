""" 
@author: GaloisField
"""

########################################################################################
##############				IMPORT STATEMENT						####################
########################################################################################


from requests import Request, Session
import json
import pprint

########################################################################################
################# 		GET LAST LISTINGS TO TEXT 					####################
########################################################################################

urlLatestListings = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parametersListings = {
	'start':1000,
	'limit':1016,
	'sort':'date_added'
}

headers = {
	'Accepts' : 'application/json',
	'X-CMC_PRO_API_KEY' : 'YOUR_CMC_API_KEY'
}

session = Session()
session.headers.update(headers)

responseListings = session.get(urlLatestListings, params=parametersListings)
latestListings = json.loads(responseListings.text)['data']


lastListing = latestListings[0]
previousListing = latestListings[1]

########################################################################################
################# 		DEFINE USEFUL CONSTANTS				############################
########################################################################################

name_lastListing = lastListing['name']
symbol_lastListing = lastListing['symbol']
contractAddress_lastListing = lastListing['platform']['token_address']
chain_lastListing = lastListing['platform']['name']
dateAdded_lastListing = lastListing['date_added']
rank_lastListing = lastListing['cmc_rank']
priceUSD_lastListing = lastListing['quote']['USD']['price']
id_lastListing = lastListing['id']


name_previousListing = previousListing['name']
symbol_previousListing = previousListing['symbol']
contractAddress_previousListing = previousListing['platform']['token_address']
chain_previousListing = previousListing['platform']['name']
dateAdded_previousListing = previousListing['date_added']
rank_previousListing = previousListing['cmc_rank']
priceUSD_previousListing = previousListing['quote']['USD']['price']
id_previousListing = previousListing['id']




