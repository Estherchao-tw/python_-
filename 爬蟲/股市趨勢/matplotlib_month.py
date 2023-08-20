import numpy as np
import pandas as pd
import matplotlib.dates as mdates    #處理日期
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import os
# 轉成csv檔
df= pd.read_csv("./2022_0056_stock/2022_0056_stock.csv")

# #趨勢圖需要 日期、價格、標題、最高價、最低價、收盤價
date = df["日期"]
high_price = df["最高價"]
low_price = df["最低價"]
end_price = df["收盤價"]

# print(date,high_price)

for i in range(0,len(date)):
  date.iloc[i]=date.iloc[i].replace(date.iloc[i][0:3], str(int(date.iloc[i][0:3]) + 1911))


date=pd.to_datetime(date,format='%Y/%m/%d' ) 
df['日期'] = pd.to_datetime(df['日期'])
date.head()

fig, ax = plt.subplots()

# # 設定中文字體
plt.rcParams['font.sans-serif'] = ["Microsoft JhengHei"]

# # 繪圖

ax.plot(date,high_price,color="#ff1122",)
ax.plot(date,low_price,color="#00bd22",linewidth=5)
ax.plot(date,end_price,color="#ff1122",linestyle = "dashed")
ax.set_xlabel("日期")
ax.set_ylabel("價格")
#設定x軸主刻度顯示格式（月/日）
# ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d"))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m"))
#設定x軸主刻度間距
# ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.legend(["最高價","最低價","收盤價"], loc="upper right")
ax.set_title("111年0056股市趨勢圖", fontsize='medium')
ax.grid(True)

plt.plot()
# 存成圖片
os.makedirs('./matplotlib_year',exist_ok=True)
plt.savefig("./matplotlib_year/2022-0056_matplotlib_chat.png")
# # 顯示圖片
plt.show()