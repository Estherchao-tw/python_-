#靜態爬蟲 套件 bs4 (BeautifulSoup4)
#需要對HTTP 做出請求的庫，叫做request


from bs4 import BeautifulSoup
import requests

# use 「request」 to ask request for certain url，傳送需求，需要對方同意才可以繼續使用該url
#User-Agent(使用者代理)，讓網站認為你是真人
response = requests.get(
  "https://ithelp.ithome.com.tw/m/users/20138060/ironman/3885", 
  headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
  })

# print(response.headers)

# 資料爬取 要取得網站上的甚麼資料，利用html.parseer(HTML解析器)來解析網站，再來因為我們要取得的是文章標題，所以形式是text。程式碼如下:
soup = BeautifulSoup(response.text, "html.parser")
data = soup.select("h3")
print(soup.title)
# print(soup.head)
print(soup.head.title)
print(soup.head.title.string)
print(soup.select("body.h3"))
print(soup.find_all('href'))
print(data)
# 迴圈爬取
for d in data:
  print(d["href"],d.text)





