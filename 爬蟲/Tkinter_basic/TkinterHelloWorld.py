#Tkinter python build GUI
#建立視窗

import tkinter as tk
from tkinter import messagebox

top = tk.Tk() #建立架構
top.title('Esther') #建立視窗名稱
top.geometry('380x400') #建立視窗大小
top.resizable(False,False) #定義不可以被放大縮小
top.iconbitmap('../images/tree/favicon.ico') #視窗圖標



def helloCallBack():
    messagebox.showinfo("Hello python","hello Esther")



B = tk.Button(top,text="Hello",command = helloCallBack)
B.pack()
top.mainloop()













