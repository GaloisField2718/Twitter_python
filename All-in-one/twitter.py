##############################################################################################################################################
########################## >>>>>>>>>>>>> Utilisation des packages Binance  <<<<<<<<<<<<<<<<<<<<<< #############
###########################################################################################################################################

# Import pour récupérer les datas
from binance.client import Client # Utilisation package python-binance
import pandas as pd
from datetime import datetime

# To shutdown pandas warnings
import warnings
warnings.filterwarnings('ignore') # setting ignore as a parameter


client = Client()

# Noms des jetons voulus
coin = 'DOGE'
fiat1 = 'USDT'
fiat2 = 'BUSD'

# Arguments pour client.get_historical_klines 
pairs = [coin+fiat1, coin+fiat2, fiat2+fiat1]
p = coin+fiat1

start = 'Yesterday'
time = client.KLINE_INTERVAL_1DAY
dataFrames = [] # Initialisation de la liste qui contiendra tout les df pour chaque paire donnée


for index in range(len(pairs)):

	klines = client.get_historical_klines(pairs[index],time,start)
	df = pd.DataFrame(klines,columns = ["timestamp","open","high","low","close","volume","close_time","quote_av","trades","tb_bas_av","tb_quotes_av","ignore"])
	df.drop(df.columns.difference(['open', 'close', 'volume']),1, inplace = True)
	df['Cours actuel'] = df['close']
	del df['close']
	df['Volume (token) '] = df['volume']
	df['Volume (USDT)'] = float(df['volume'])*float(df['Cours actuel'])
	del df['volume']
	df['Variation %'] = 100*(1-(float(df[('open')])/float(df['Cours actuel'])))
	df.columns = ['Cours ouverture','Cours actuel','Volume (token)','Volume (USDT)', 'Variation %']

	dataFrames.append(df)



# Récupérer et nommer chacune des colonnes de dataFrames.
lenght = len(dataFrames)
cours = [round(float(dataFrames[index]['Cours actuel']),8) for index in range(lenght)]
variations = [round(float(dataFrames[index]['Variation %']),2) for index in range(lenght)]
volumeToken = [round(float(dataFrames[index]['Volume (token)']),3) for index in range(lenght)]
volumeUSDT = [round(float(dataFrames[index]['Volume (USDT)']),3) for index in range(lenght)]


print(cours)

currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%D, à l'heure %H:%M:%S")





########################################################################################################################################
################################>>>>>>>>>>>>>>>>>> Classe MESSAGES <<<<<<<<<<<<<<<########################################
########################################################################################################################################

""" COMMENTAIRES
 
- J'ai retiré la comparaison {fiat2}/{fiat1} car le message est trop long. 

"""

debutMessage = f"Le cours sur Binance du {coin}/{fiat1}, à la date du {currentTime} est : {cours[0]}, pour une variation de "
variationMessage = f"{variations[0]}%. \n"


# Force l'affichage du + quand la variation est positive.
if variations[0] > 0 :
	message = f"{debutMessage} +{variationMessage}"
else :
	message = f"{debutMessage} {variationMessage}"
	

infos = "Ceci est un message automatisé par #script #Python."

message = message+"\n"+infos

messageVolume = f'Les volumes de la paire {coin}/{fiat1} sont de {volumeToken[0]}.\n Ceci en date du {currentTime}.'

messageHashtag = '#BTC #DOGE #DOGECOIN #Crypto #Market #marketcrypto #Binance #BNB #Trading #Volume #BearMarket #Python #Automation #Script #AWS #Tweepy '

messageQuestion = 'Let me know if you want other pairs 😜 @elonmusk'

alertePositiveVolatility = f"Beaucoup de volatilité en cette tumultueuse journée. #WARNING #{coin} #Volatility #PROFITS.\n Plus de 20% de hausse !!"
alerteNegativeVolatility = f"Beaucoup de volatilité en cette tumultueuse journée. #WARNING #{coin} #Volatility #RISKS.\n Plus de 20% de baisse !!"

print(message, "\n", messageVolume, "\n")


###############################################################################################################################################

##################### >>>>>>>>>>>>>> Main <<<<<<<<<<<<<<<<<< ###########################################################################

#############################################################################################################################################


from urllib import response
import config
import tweepy


# Tweepy client initialisation
# Initialisation du client Tweepy
client = tweepy.Client(consumer_key=config.API_KEY, consumer_secret=config.API_KEY_SECRET, access_token=config.ACCESS_TOKEN, access_token_secret=config.ACCESS_TOKEN_SECRET)


# Create the first tweet with price informations
# Crée le premier tweet avec les informations des cours
response = client.create_tweet(text=message)
print(f"https://twitter.com/user/status/{response.data['id']}\n")

# Create an answer to first tweet with the volumes
# Crée une réponse au premier tweet avec les volumes
responseVolume = client.create_tweet(in_reply_to_tweet_id=response.data['id'], text=messageVolume)
print(f"https://twitter.com/user/status/{responseVolume.data['id']}\n")

# Comment with an alert message if variations[0]>20%
# Alerte si les variations sont supérieures à 20%
if variations[0] > 20 :
	responsePositiveVolatility = client.create_tweet(in_reply_to_tweet_id=responseVolume.data['id'], text=alertePositiveVolatility)
	print(f"https://twitter.com/user/status/{responsePositiveVolatility.data['id']}\n")

if variations[0] < -20 :
	responseNegativeVolatility = client.create_tweet(in_reply_to_tweet_id=responseVolume.data['id'], text=alerteNegativeVolatility)
	print(f"https://twitter.com/user/status/{responseNegativeVolatility.data['id']}\n")

# Comment with the hashtag line
# Commente avec les Hashtags
responseHashtag = client.create_tweet(in_reply_to_tweet_id=responseVolume.data['id'], text=messageHashtag)
print(f"https://twitter.com/user/status/{responseHashtag.data['id']}")

responseQuestion = client.create_tweet(in_reply_to_tweet_id=responseHashtag.data['id'], text=messageQuestion)
print(f"https://twitter.com/user/status/{responseQuestion.data['id']}")


""" We can use only the Bearer Token to make a tweet query """

# bearer_token = config.BEARER_TOKEN
# query = 'Blockchain NearProtocol'

# response = client.search_recent_tweets(query = query, max_results = 10)

# print(response)





# TODO : Coder une soustraction pour les chaines de caractères (string). En faire une OPERATION := - , pas qu'une fonction. 

