# Stock price analysis with Python

It's crucial for investors to understand the risk of investing in the stock market. A company's stock price reflect its evaluation and performance, which influences the demand and supply in the market. Technical analysis of the stock is a vast field ,and  I will provide an overview of it in this REAME.me 

Let's dive into the stock price analysis with Python 

**installation** 

import numpy as np <br>
import pandas as pd <br>
import matplotlib.dates as mdates    #處理日期<br>
import matplotlib.pyplot as plt<br>
import matplotlib.cbook as cbook<br>

**Data Description**

We have downloaded the daily stock prices data using the TWSE API functionality. It’s an year data capturing Open, High, Low, Close, and Volume

[開盤價]Open: The price of the stock when the market opens in the morning
[收盤價]Close: The price of the stock when the market closed in the evening
[最高點]High: Highest price the stock reached during that day
[最低點]Low: Lowest price the stock is traded on that day
[成交股數]Volume: The total amount of stocks traded on that day
[成交數量]Number of transaction

Here, we will take the Example of stock 0056 which are the ETF leaders in providing IT services.

### stock prices of 0056| stock price analysis python

This graph is clearly shows that the highest price of 0056 is more when comparing it to other two index but I'm not interested in the absolute prices for these index but wanted to understand how these stock fluctuate with time

![2022-0056_matplotlib_chat](https://github.com/Estherchao-tw/python_-/assets/74496288/9d04ead5-12ab-4c10-8459-ee3acbcf5f70)

![May-0056_matplotlib_chat](https://github.com/Estherchao-tw/python_-/assets/74496288/58eec5c0-c2d7-4e58-9636-840ae44ccd6e)


### Python code explation

Step:

- 分析網頁結構
- 開發Python網頁爬蟲
- Pandas 儲存csv 資料
- Python網頁爬蟲讀取csv資料

[^hint]: first to third steps is in "year_stock.py" and fourth step is in "matplotlib_month.py"

一、分析網頁結構

分析TWSE 的網站，我們透過一般的爬取方式，取複製requests url 利用 request module 發送get 請求到url的網站，並透過json() function ，將json轉成python dictionary ，存取data(查詢的結果)

```py
    
    url =  "https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date=2022{:02d}01&stockNo=0056&response=json&_=1689749700657".format(m)
    #格式化字符函數 str.format()，透過 {} 和 format 來代替 %運算符號
    response = requests.get(url)
    js_data = json.loads(response.text)
```

二、開發Python 網頁爬蟲

透過迴圈讀取以上的網頁回應資料

```python
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

```

三、Pandas 儲存csv 資料

將data資料轉成pandas dataframe export to csv

```python
year_df = pd.DataFrame(data,columns=fields0)
print("2022 stock df")
```

轉成csv檔

可以p.head() 看看是不是資料存的正確

```
os.makedirs('./2022',exist_ok=True)
year_df.to_csv("./2022/2022_year_stock.csv",encoding="utf-8-sig")
p = pd.read_csv('./2022/2022_year_stock.csv')  
print(p.head()) 
```

四、Python網頁爬蟲讀取csv資料

[^hint]: in [matplotlib_month.py]

趨勢圖需要 日期、價格、標題、最高價、最低價、收盤價

```python
date = df["日期"]
high_price = df["最高價"]
low_price = df["最低價"]
end_price = df["收盤價"]
```

設定中文字體

```python
plt.rcParams['font.sans-serif'] = ["Microsoft JhengHei"]
```

Plot 繪圖

```python
fig, ax = plt.subplots()

ax.plot(date,high_price,color="#ff1122",)
ax.plot(date,low_price,color="#00bd22",linewidth=5)
ax.plot(date,end_price,color="#ff1122",linestyle = "dashed")
ax.set_xlabel("日期")
ax.set_ylabel("價格")
#設定x軸主刻度顯示格式（月/日）
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d"))
#設定x軸主刻度間距
ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
ax.legend(["最高價","最低價","收盤價"], loc="lower right")
ax.set_title("112年5月股市趨勢圖", fontsize='medium')
ax.grid(True) 
```

plt.plot()

存成圖片

```python
plt.savefig("5_matplotlib_chat.png")
```

顯示圖片

```python
plt.show()
```



### Conclution 

the above analysis can be used to understand a stock's short term and basic behavior. A decision support system can be created which stock to pick from industry for low-risk  gain or high-risk gain.

