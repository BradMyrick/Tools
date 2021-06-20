import json
import urllib.request

currency = 'https://v6.exchangerate-api.com/v6/a54f7d46035b54ec17a14edb/pair/USD/COP'
a = 'https://api.coingecko.com/api/v3/coins/'
coins = ['bitcoin', 'ethereum', 'binancecoin', 'dogecoin']
c = '?localization=false&tickers=false&community_data=false&developer_data=false&sparkline=false'
tracked = []
feed = []
update = bool
separate = ''
def getCoin(coins):
    for i in range(len(coins)):
        b = coins[i]
        with urllib.request.urlopen(a+b+c) as url:
            data = json.loads(url.read().decode())
            rate = data.get('market_data').get('current_price').get('usd')
            info = ('USD to 1 ', str(b), ' : ', str(rate))
            info = separate.join(info)
            feed.append(info)
            if update:
                tracked.append(info)

if __name__ == '__main__':
    print('Wealthy Wallet Asset Tracker')
    with open("trackedCoins.txt", "r") as fp:
        savedFile = json.load(fp)
    getCoin(coins)
    for coin in feed:
        print(coin)
    print("Your Tracked Prices:")
    for items in savedFile:
        print(items)
    print("Would you like to update saved prices? ")
    print("1) YES : 2) NO")
    x = int(input("Number Only: "))
    if x == 1:
        with open("trackedCoins.txt", "w") as fp:
            json.dump(tracked, fp)


