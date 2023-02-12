"""	
@author: GaloisField2718

""" 
import prices
from datetime import datetime

"""
@param1 : symbol
@note : Let be sure to take enough limit in prices.parameters option and your symbol
 is inside range.
"""
symbol = 'NEAR'

"""
 Very important part ! Everything after will depend on those constants.
"""
data = prices.data
index = prices.getIndexFromSymbol(data,symbol)

"""
 Use functions defines in prices.
"""
cmcRank = data[index]['cmc_rank']
marketCap = round(data[index]['quote']['USD']['market_cap'],3)
marketCap = prices.metLesVirgules(marketCap)
price = round(data[index]['quote']['USD']['price'],3)

"""
@param2 : first frequency

"""
frequency = '24h' 
percentChange = round(prices.getPercentChange(data,frequency,symbol),2)
plusMoins = prices.signPercentChange(data,frequency,symbol)

"""
@param3 : second frequency
"""
freq2 = '30d'
percentChange2 = round(prices.getPercentChange(data,freq2,symbol),2)
plusMoins2 = prices.signPercentChange(data,freq2,symbol)


currentTime = datetime.now()
""" 
@todo : Get french date  d/m/Y. I don't understand why it doesn't work.
"""
now = currentTime.strftime("%D, à %H:%M:%S")




message1 = f"A la date du {now}, #{symbol} est classée {cmcRank}ℹ️ème sur #CoinMarketCap"

message2 = f"Sa #marketCap est de 💵{marketCap} avec une variation de {plusMoins}{percentChange}% en {frequency} & {plusMoins2}{percentChange2}% en {freq2}."

message3 = f"Son prix est de 💰{price}.\n \n #NEARProtocol #Crypto #CMC #BTC #Market #MarketWatch #Trading #Bot #Python #Algorithm #Finance #Future #REFI #Binance #Alert #Automation #CryptoFR"



print(message1)

print(message2)

print(message3)



















