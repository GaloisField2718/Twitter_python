""" 
L'idée étant qu'un agrégateur doit être une meilleure solution pour avoir 
la capitalisation boursière des cryptos que les exchanges.

"""

from requests import Request, Session
import json
import pprint

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
	'start':'1',
	'limit':'5000',
	'convert':'USD'
}

headers = {
	'Accepts' : 'application/json',
	'X-CMC_PRO_API_KEY' : 'e3763607-e592-4ba9-b6d5-3769d4a54290'
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)

data = json.loads(response.text)['data']

# Pour vérifier le contenu de data
#pprint.pprint(data)


def getIndexFromSymbol(data,symbol):
	lenght = len(data)
	for index in range(lenght):
		if(data[index]['symbol']==symbol):
			return index
		else :
			index+=1
	return "No matches found with this symbol"


# A améliorer car dépendante du code au-dessus
def getCMCRankFromSymbol(data,symbol):
	lenght = len(data)
	index = getIndexFromSymbol(data,symbol)
	try :
		index==int(index)
		return data[index]['cmc_rank']

	except ValueError:
		return "ERROR : index not found"


symbol = 'NEAR'



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

		valueDecimale = str(value)
		textValue = str(value)
		textIntValue = str(int(value))

		for index in range(len(textIntValue)):
			valueDecimale = valueDecimale.replace(textValue[index],"")

		valueEntiere = metLesVirgules(int(value))

		value = f"{valueEntiere}{valueDecimale}"

		return value



