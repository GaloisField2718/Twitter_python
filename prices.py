""" 
@author: GaloisField

@params : Your CoinMarketCap API KEY

"""

from requests import Request, Session
import json
import pprint

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

###########################################################################
############				Parameters						############### 		
###########################################################################
"""
@note : These are parameters for /listings/latest if one changes url 
		parameters should change
""" 
parameters = {
	'start':'1',
	'limit':'100',
	'convert':'USD'
}

"""
@note : This should be the same for every url.
"""
headers = {
	'Accepts' : 'application/json',
	'X-CMC_PRO_API_KEY' : 'YOUR_API_KEY'
}

###########################################################################
#################			Connexion 						###############
###########################################################################
session = Session()
session.headers.update(headers)
response = session.get(url, params=parameters)

"""
@note : Most important object for our interest.
"""
data = json.loads(response.text)['data']

"""
@note You should try this one to take an overview about data
"""
#pprint.pprint(data)

###########################################################################
#############		Functions to simplify messages 			###############
###########################################################################


def getIndexFromSymbol(data,symbol):
	lenght = len(data)
	for index in range(lenght):
		if(data[index]['symbol']==symbol):
			return index
		else :
			index+=1
	return "No matches found with this symbol"


"""
@todo :  Improve this function because is dependent of the above function.
"""
def getCMCRankFromSymbol(data,symbol):
	lenght = len(data)
	index = getIndexFromSymbol(data,symbol)
	try :
		index==int(index)
		return data[index]['cmc_rank']

	except ValueError:
		return "ERROR : index not found"


def getIndexFromRank(data,cmc_rank):
	lenght = len(data)
	for index in range(lenght):
		if(data[index]['cmc_rank']==cmc_rank):
			return index
		else :
			index +=1
	return "ERROR : No index found for this rank"

def getSymbolFromRank(data,cmc_rank):
	index = getIndexFromRank(data,cmc_rank)
	return data[index]['symbol']


def getPercentChange(data,frequency,symbol):
	# Transforme la chaîne frequency en minuscule
	frequency = frequency.lower()
	# Choisit le bon pourcentage avec match variable: case...
	match frequency:
		case '1h':
			frequencyChange = f"percent_change_1h";
		case '24h':
			frequencyChange = f"percent_change_24h";
		case '7d':
			frequencyChange = f"percent_change_7d";
		case '30d':
			frequencyChange = f"percent_change_30d";
		case '60d':
			frequencyChange = f"percent_change_60d";
	
	index = getIndexFromSymbol(data,symbol)

	percentChange = data[getIndexFromSymbol(data,symbol)]['quote']['USD'][frequencyChange]

	return percentChange




# Renvoie la string + si changement > 0 et la chaine vide sinon
def signPercentChange(data,frequency,symbol):

	percentChange = round(getPercentChange(data,frequency,symbol),2)
	index = getIndexFromSymbol(data,symbol)

	if percentChange>0:
		plusMoins = f"+"
	else:
		plusMoins = f""

	return plusMoins

def signValue(value) : 
	if value > 0 :
		plusMoinsSymbol = f"+"
	else :  
		plusMoinsSymbol = f""
	return plusMoinsSymbol



###########################################################################
############## 		Mise en page pour les grands nombres 		###########
###	@note:j'ai appris qu'il existait des fonctions pour faire ceci ########
## 				mais ce code peut me servir un jour...			###########	
###########################################################################


# Il faut calculer le nombre de chiffres après la virgule pour la fonction metsLesVirgules
def getNombreChiffresApresVirgule(value):
	valueInt = str(int(value))
	value = str(value)

	nombreChiffresApresVirgule = len(value)-len(valueInt)

	return nombreChiffresApresVirgule


# Fais la même chose que "{:=,}".format(value) 
def metLesVirgules(value):

	# Si value est un nombre entier on applique la fonction
	if value == int(value):

		value = str(value)
		lenght = len(value)
		nombreReecris = f""

		index = 0

		if lenght<4:
			nombreReecris = f" {value} "
		
		else:

			if lenght%3 == 0:
				while index<lenght:
					if index == lenght-3:
						nombreReecris = nombreReecris+f"{value[index]}{value[index+1]}{value[index+2]}"
						index+=3
					else:
						nombreReecris = nombreReecris+f"{value[index]}{value[index+1]}{value[index+2]} "	
						index += 3

			if lenght%3 == 1:
				nombreReecris = f" {value[index]} "
				index +=1
				while index<lenght:
					if index == lenght-3:
						nombreReecris = nombreReecris+ f"{value[index]}{value[index+1]}{value[index+2]}"
						index+=3
					else:
						nombreReecris = nombreReecris+ f"{value[index]}{value[index+1]}{value[index+2]} "	
						index+=3

			if lenght%3 == 2:
				nombreReecris = f" {value[index]}{value[index+1]} "
				index += 2
				while index<lenght:
					if index == lenght-3:
						nombreReecris = nombreReecris+ f"{value[index]}{value[index+1]}{value[index+2]}"
						index+=3
					else:
						nombreReecris = nombreReecris+ f"{value[index]}{value[index+1]}{value[index+2]} "	
						index+=3
			return nombreReecris
	else :
		# Pour éviter de calculer a-int(a), je convertit en chaîne de caractère a puis j'enlève len(int(a)) sur les premiers caractères
		"""
			@note : a-int(a) ≠ decimal(a) because there are some little variations 
					in the float such that : we can't compute by the arithmetic way 
					this difference.
		"""
		valueDecimale = str(value)
		textValue = str(value)
		textIntValue = str(int(value))

		for index in range(len(textIntValue)):
			valueDecimale = valueDecimale.replace(textValue[index],"")

		valueEntiere = metLesVirgules(int(value))

		value = f"{valueEntiere}{valueDecimale}"

		return value



