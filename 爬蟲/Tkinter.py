#Tkinter python build GUI
#建立視窗

import tkinter as tk
from tkinter.constants import *


window = tk.Tk() #建立架構
window.title('Esther') #建立視窗名稱
window.geometry('380x400') #建立視窗大小
window.resizable(False,False) #定義不可以被放大縮小
window.iconbitmap('./images/tree/favicon.ico') #視窗圖標



###布局{pack,grid,place}
## pack
# side:top,button,right,left
# window = tk.Button(text="我愛你")
# window.pack(side="top",fill="both")

# window = tk.Button(text="I")
# window.pack(side="left")

# window = tk.Button(text="Love")
# window.pack(side="left")


# window = tk.Button(text="You")
# window.pack(side="right")

# window = ANCHOR()#anchor : 用來設定元件起始位置(錨定位置)，有E,W,S,N,CENTER,NE,SE,SW,NW

## grid 
# #  row and column
# window = tk.Button(text="column1")
# window.grid(row=10,column=10)

# window2 = tk.Button(text="row1column15")
# window2.grid(row=20,column=15)

# window3 = tk.Button(text="column23")
# window3.grid(row=30,column=23)

##place
# 絕對位置

test = tk.Button(text="testing")
test.place(x=190,y=300,anchor=CENTER)

















window.mainloop() #重要!使城市常駐執行

# test = tk.Button(text="testbutton")
