import requests
import json
import pandas as pd

for m in range(1,13):
    
    url =  "https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date=2023{:02d}01&stockNo=0056&response=json&_=1689749700657".format(m)
    #格式化字符函數 str.format()，透過 {} 和 format 來代替 %運算符號
    #  The format specification can be written after : in {}.
    # print(url)
    
    payload = ""
    headers = {
      'Cookie': 'JSESSIONID=9BED9ED6A04B81A20BB4D82747EAF92A'
    }

    response = requests.get(url)


    js_data = json.loads(response.text)
    data0 = js_data['data']
    fields0 = js_data['fields']
    print(type(data0))
    


# # 將資料轉成dataframe export to csv
# # use Pandas
    mon_df = pd.DataFrame(data0,columns=fields0)
    year_df = pd.concat(mon_df,ignore_index=True)
    print(type(year_df))


# 轉成csv檔
#將每個月的DataFrame合併成一個整年的DataFrame。ignore_index=True讓合併後資料的index是連續的。
    year_df.to_csv("./year_stock.csv",encoding="utf-8-sig")
# 轉成xlsx檔
# # df.to_excel("./month_stock.xlsx")
# 轉成html檔
# # df.to_html("./month_stock.html")

