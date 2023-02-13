# Twitter python


## ✅ Setup

### Requirements

**python packages**

👉 `pip3 install urllib`

👉 `pip3 install requests`

👉 `pip3 install json`

👉 `pip3 install pprint` *This is to get data in an easy reading way.*

👉 `pip3 install tweepy` **Main Package to make tweets !**

**cron**

👉 `npm install cron` See [Downloading and installing Node.js
and npm | npm Docs](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
for more details about `npm`

**TESTING integration**
👉 `pip3 install textwrap`

If you have some of those packages, download only necessary ones.

### Steps

1️⃣ `git clone https://github.com/GaloisField2718/Twitter_python`

2️⃣ Get your Twitter API Keys on [Twitter dev Portal](https://developer.twitter.com/en/portal). You will pass your twitter account in twitter dev account.

3️⃣ Add your keys in  `dogeaccountpy/config.py` file.

4️⃣ Get your API-key in CoinMarketCap and put it in `dogeaccountpy/prices.py` (it's indicated in the code). 

5️⃣ You can change messages in `dogeaccountpy/messages.py`.

6️⃣ You can make a first try with : 
```bash
python3 tweets.py
```

7️⃣ Automation with cron :
When you have cron you can launch on your computer a command like which provided in 
`crontab.txt` file.


## 🎯 Goal

### 1. 🙌 Give the code which is running on Twitter

I created two twitter account : [@Marketcryptopy](https://twitter.com/marketcryptopy) and [@dogeaccountpy](https://twitter.com/dogeaccountpy) which is running since few month and I want to share this code. 

It's not strong coded and we can improve it in several differents ways but for now it works and that's cool 😎.

I will briefly details after what I used to get cryptocurrencies prices 🤑, what config we need to use with tweepy and basic tweepy commands.

### 2. 🐚 Give some advice to use Twitter on python3 command-line

I also want to provide the basic shell commands I use to interact with *[@Marketcryptopy](https://twitter.com/marketcryptopy)* on my console. 
I'm trying to use this account only in command line and never interact through Twitter interface. Sometimes it's harder but it's fun to see it's possible.

# ADDED COINMARKETCAP (CMC) LAST LISTINGS

🧪 I tried to connect CMC API with `latest Listings url`, `metadata url` and `tweepy` to get information about new CMC listings. Especially get important data as website, description, social medias,...

㊷ Unfortunately, the `textwrap` python which I used seems to not produce convienent output :

```
Your Tweet text is too long. For more information on how Twitter determines text length see https://github.com/twitter/twitter-text.
```
I'm working hard on this issue to produce soon 🔜 a working bot for this job.

## 🔩 Tools

### 1. 💰 Get prices

To get prices I use 2 differents API :

👉 *MarketCryptoPy* : **CoinMarketCap-API**.
 
📜 The unofficial documentation : [python-binance](https://python-binance.readthedocs.io/en/latest/) but it's quite hard to onboard through this. There is an incredible Youtube Channel [@cryptorobotfr](https://www.youtube.com/@cryptorobotfr), they are french but you can translate the video and their code is in english so don't worry 😁.

📺 One very good video to begin with python-binance package [[TUTO FR] Créer son PROPRE BOT DE TRADING CRYPTO facilement en Python !](https://www.youtube.com/watch?v=_gNIWHh539A&t=1221s) and the associated github repo [create personnal trading bot](https://github.com/CryptoRobotFr/1-create-personnal-trading-bot).


👉 *DogeAccountPy* : **python-binance**.

📜 Documentation : [CoinMarketCap API Documentation](https://coinmarketcap.com/api/documentation/v1)

📺 Youtube channels can help you to onboard with CoinMarketCap API.

🔍 Looking for optimization [Le Design Pattern Contre-Intuitif le plus utilisé par les Développeurs Professionnels](https://youtu.be/zto9F3ANVXA).--


### 2. 🐣 Tweepy

To onboard with this package you definitely should see this video 
📺 [How to use the Twitter API v2 in Python using Tweepy](https://www.youtube.com/watch?v=0EekpQBEP_8&t=1961s).
All my **Tweepy** code is based on this video !



### 3. 🤖 Automation

The automation is made with [cron - npm](https://www.npmjs.com/package/cron).
It's an automation tool in command line that you can install easily with : 
`npm install cron`.

After you install it you can check some use on [crontab.guru](https://crontab.guru/#*_1_*_*_*).

I provide a `crontab` file without extension which can be open by every text editor. It's a basic syntax but this file provide a solution when your shell doesn't find the good python compiler.

This automation actually runs on AWS EC2 Instance with a *free account* but I think it will be removed soon because I don't want to pay!

Still in french you can find a good detail about how to deploy an AWS free instance [[Tuto FR] Héberger votre BOT DE TRADING crypto GRATUITEMENT en Python sur un serveur avec FTX](https://www.youtube.com/watch?v=TbZ9BVAW_SA).



## Structure

### 1. PricesByCMC

👉 **config.py** : which stores every twitter access keys.

👉 **prices.py** : which ask prices at *CoinMarketCap* and provide some functions to simplify messaging and accessing data. There is also a function `metsLesVirgules` which makes the same thing as `"{:=,}".format(value)` but I didn't know so I hardcoded this function and I let here.

👉 **messages.py** : uses every functions in prices to provide 3 messages.

👉 **tweets.py** : the last one obviously... to TWEET PRICES 🤑 ‼️

👉 **crontab** : the file where the command is stored to automate post.

### 2. PricesByBinance

This uses python-binance package, and contains only two files : 

👉 **Twitter.py** : it's my first file and contains Binance prices call, messages and tweeting via tweepy.

👉 **config.py** : still a config file to run all of this.


### 3. NewListingOnCMC

👉 **listings_cmc.py** : make the call to get latest CMC listings.

👉 **metadata_listings.py** : provide metadata related to latest listings taking from `listings_cmc.py`.

👉 **tweets_wrapper.py** : a simple file which contains one function : `tweets_wrapper`.

#### I think problems raised from tweets_wrapper or tweets. If someone is available to chat about this it will be a pleasure 😄

👉 **tweets.py** : obviously posting file, but also some textual operations to improve each threads.
