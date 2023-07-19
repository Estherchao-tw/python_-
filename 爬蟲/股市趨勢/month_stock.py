import requests
import json
import pandas as pd

url = "https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date=20230719&stockNo=0056&response=json&_=1689749700657"
response = requests.get(url)

# print(response.text)
js_data = json.loads(response.text)
data0 = js_data['data']
fields0 = js_data['fields']
# print(js_data)
print(type(data0))


# 將資料轉成dataframe export to csv
# use Pandas
df = pd.DataFrame(data0,columns=fields0)
print(type(df))


# 轉成csv檔
df.to_csv("./month_stock.csv",encoding="utf-8-sig")
# 轉成xlsx檔
df.to_excel("./month_stock.xlsx")
# 轉成html檔
df.to_html("./month_stock.html")

