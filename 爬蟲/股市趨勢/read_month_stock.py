import pandas as pd

# 轉成csv檔
df= pd.read_csv("./May_0056股票/5_month_stock.csv")
# 轉成xlsx檔
# df1 = pd.read_excel("./5_month_stock.xlsx")
# # 轉成html檔
# df2 = pd.read_html("./5_month_stock.html")

# print(df0,df1,df2)

# print(df)

#趨勢圖需要 日期、價格、標題、最高價、最低價、收盤價
date = df["日期"]
print(type(date))
print(date)
high_price = df["最高價"]
low_price = df["最低價"]
end_price = df["收盤價"]

