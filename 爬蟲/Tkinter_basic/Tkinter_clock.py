import tkinter as tk
import datetime

# 定義產生不同時區時間的函式
  #dt.timedelta:兩個datetime 物件的不同
  #specify the tz argument to a valid time zone object
def timezone_(h):
    GMT = datetime.timezone(datetime.timedelta(hours=h)) #取得時區
    now = datetime.datetime.now(tz=GMT).strftime('%H:%M:%S') #取得現在時間
    return now

# 創建視窗
root = tk.Tk()
root.title('各地時區')
root.geometry('280x480')

# 在視窗中創建字串string 
name = [ '台灣', '日本','美國加州', '美國德州']
loc_time=[8,9,-8,-6]
arr = [tk.StringVar() for i in range(4)] ## 使用串列生成式，產生一個內容包含四個 tk 文字變數的串列


#定義顯示時間的函式
def showTime():
    #因為有四個時間，巡迴四次
    for i in range(4):
        arr[i].set(timezone_(loc_time[i])) #設定文字變數，要放進arr變數形成tk變數string
    root.after(1000, showTime) # execute showTime() every 1000ms

# 利用迴圈跑4次，在視窗中顯示地區與時間
for i in range(4):
    tk.Label(root ,text=name[i], font=('Arial',32)).pack()
    tk.Label(root,textvariable=arr[i],font=('Arial',20)).pack()


showTime()
root.mainloop()