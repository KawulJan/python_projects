import requests

URL = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=7203.T"
TARGET = "stocksPrice"
res = requests.get(URL)
lines = res.content.decode("utf-8").split("\n")
line = [l for l in lines if "stocksPrice" in l][1]
print(line[line.find(">") + 1:-5])
