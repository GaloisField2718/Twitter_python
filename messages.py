import prices
from datetime import datetime


symbol = 'NEAR'
data = prices.data
index = prices.getIndexFromSymbol(data,symbol)

cmcRank = data[index]['cmc_rank']
marketCap = round(data[index]['quote']['USD']['market_cap'],3)
marketCap = prices.metLesVirgules(marketCap)

price = round(data[index]['quote']['USD']['price'],3)
frequency = '24h'
percentChange = round(prices.getPercentChange(data,frequency,symbol),2)
plusMoins = prices.signPercentChange(data,frequency,symbol)

freq2 = '30d'
percentChange2 = round(prices.getPercentChange(data,freq2,symbol),2)
plusMoins2 = prices.signPercentChange(data,freq2,symbol)


currentTime = datetime.now()
# Régler la date pour avoir J/M/A
now = currentTime.strftime("%D, à %H:%M:%S")




message1 = f"A la date du {now}, #{symbol} est classée {cmcRank}ℹ️ème sur #CoinMarketCap"

message2 = f"Sa #marketCap est de 💵{marketCap} avec une variation de {plusMoins}{percentChange}% en {frequency} & {plusMoins2}{percentChange2}% en {freq2}."

message3 = f"Son prix est de 💰{price}.\n \n #NEARProtocol #Crypto #CMC #BTC #Market #MarketWatch #Trading #Bot #Python #Algorithm #Finance #Future #REFI #Binance #Alert #Automation #CryptoFR"



print(message1)

print(message2)

print(message3)



















