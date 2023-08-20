import requests
import json
import pandas as pd
import os
from fake_useragent import UserAgent
import socket
import random

 
socket.setdefaulttimeout(10) 

data =[]
ua = UserAgent()

pf = pd.read_csv('../../py-proxy/proxyIP.csv')
proxyIps = pf['proxyIP']
count = 0
for proxyIp in range(2):
    try:
        #隨機取得IP
        proxyIp = random.choice(proxyIps)
        print(proxyIp)
        # proxy ip 替換

        for m in range(1,13):
            
            url =  "https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date=2022{:02d}01&stockNo=0056&response=json&_=1689749700657".format(m)
            #格式化字符函數 str.format()，透過 {} 和 format 來代替 %運算符號
            #  The format specification can be written after : in {}.
            # print(url)
                    
            headers = {
            "Content-Type" : "application/json/json;charset=UTF-8",
            "X-Application-Context": "application:production",
            "Accept-Encoding": "gzip, deflate, br", 
            "Accept-Language": "zh-TW,zh;q=0.9", 
            "User-Agent": ua.random
            }
            response = requests.get(url,headers=headers,proxies={'https':proxyIp ,'https': proxyIp})
            print(response``.request.headers)

            js_data = json.loads(response.text)
            # print(js_data)
            stock = js_data["data"]
            fields0 = js_data["fields"]
            # detail = stock[日期][項目]
            print(stock[0])

            N = len(stock)
            for i in range(0,N-1):
                date = stock[i][0]
                trading_volume = stock[i][1] #成交股數 Trading Volume 
                transaction= stock[i][2]
                opening_price= stock[i][3]
                highest_price= stock[i][4]
                lowest_price= stock[i][5]
                closing_price= stock[i][6]
                change= stock[i][7]
                NT= stock[i][8] #成交筆數 (Number of Transactions)
                data.append([date,trading_volume,transaction,opening_price,highest_price,lowest_price,closing_price,change,NT])

        
            # print(type(stock))
        # print(type(data),type(fields0))
        # print(data)
        # # 將資料轉成dataframe export to csv
        # # # use Pandas
        year_df = pd.DataFrame(data,columns=fields0)
        print("2022 stock df")
        # 轉成csv檔
        os.makedirs('./2022',exist_ok=True)
        year_df.to_csv("./2022/2022_year_stock.csv",encoding="utf-8-sig")
        p = pd.read_csv('./2022/2022_year_stock.csv')  
        # print(p)

    except:
        print("ERROR")
