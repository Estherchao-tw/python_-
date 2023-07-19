import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://ithelp.ithome.com.tw/articles?tab=hot",
    headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    })

#print(response.headers)

soup = BeautifulSoup(response.text, "html.parser")
data = soup.select("h3.qa-list__title a")
print(data)
for d in data:
    print(d["href"], d.text)  #取<a>標籤中的href : d["href"]
    # print(d.("href"), d.text) 要取<a>標籤中的href的不同寫法，it works.
