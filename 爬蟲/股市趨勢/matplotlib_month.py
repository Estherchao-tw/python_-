import numpy as np
import pandas as pd
import matplotlib.dates as mdates    #處理日期
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
# 轉成csv檔
df= pd.read_csv("./5_month_stock.csv")

# #趨勢圖需要 日期、價格、標題、最高價、最低價、收盤價
date = df["日期"]
high_price = df["最高價"]
low_price = df["最低價"]
end_price = df["收盤價"]

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
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d"))
#設定x軸主刻度間距
ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
ax.legend(["最高價","最低價","收盤價"], loc="lower right")
ax.set_title("112年5月股市趨勢圖", fontsize='medium')
ax.grid(True)

plt.plot()
# # 存成圖片
plt.savefig("5_matplotlib_chat.png")
# # 顯示圖片
plt.show()