import tkinter as tk
import datetime

# 定義產生不同時間的函式
def timezone(h):
    GMT = datetime.timezone(datetime.timedelta(hours=h)) #取得時區
    now = datetime.datetime.now(tz=GMT).strftime('%H:%M:%S') #取得現在時間
    return now

root = tk.Tk()
root.title('各地時區')
root.geometry('280x480')

name = [ '台灣', '日本','美國加州', '美國德州']
loc_time=[8,9,-8,-6]
arr = [tk.StringVar() for i in range(4)]


#定義顯示時間的函式
def showTime():
    #因為有四個時間，巡迴四次
    for i in range(4):
        arr[i].set(timezone(loc_time[i]))
    root.after(1000, showTime) # execute showTime() every 1000ms


for i in range(4):
    tk.Label(root ,text=name[i], font=('Arial',32)).pack()
    tk.Label(root,textvariable=arr[i],font=('Arial',20)).pack()


showTime()
root.mainloop()