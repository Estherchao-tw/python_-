from tkinter import *
import tkinter  as tk
from PIL import Image,ImageTk

down = tk.Tk()
down.title('GUI')
down.geometry('480x560')
down.resizable(False,False)
down.iconbitmap('./images/tree/favicon.ico')  


# def plus():
    # print("you press the button.")

# def show():
#     password= test.get()
#     print(password)

def display1():
    print("input for good day",var1.get())
    print("input for",var0.get())
    print("input for awful day",var2.get())

#define empty variables
var0 = tk.IntVar()
var1 = tk.IntVar()
var2 = tk.IntVar()
radioVar = tk.IntVar()



#按鈕顯示文字
# up = tk.Button(text='press me',command=plus)
# up.pack()

#按紐顏色
# test = tk.Button(text="it's a yellow button",bg="yellow")
# test.place(x=100,y=100)


#輸入框 + 按鈕
# test = tk.Entry(show="*")
# test.pack()
# testButton = tk.Button(text="show",command=show)
# testButton.pack()

#checkbutton
test = tk.Checkbutton(down,text= "it's a good day",state="normal",variable=var1, onvalue=1, offvalue=0, command=display1)
test.pack()
test1 = tk.Checkbutton(down,text="it's a bad day",state="disabled",variable=var0, onvalue=1, offvalue=0, command=display1)
test1.pack()
test2 = tk.Checkbutton(down,text="it's a awful day",state="normal",variable= var2,onvalue=1, offvalue=0, command=display1)
test2.pack()

# 圓形按鈕radiobutton
radio0 = tk.Radiobutton(text='餐點A',variable=radioVar,value=0)
radio1 = tk.Radiobutton(text='餐點B',variable=radioVar,value=1)
radio2 = tk.Radiobutton(text='餐點C',variable=radioVar,value=2)

radio0.pack()
radio1.pack()
radio2.pack()

# labal 標籤，一個空盒子，可以放文字照片等
var = StringVar()
label = tk.Label(textvariable=var,relief=RAISED)

var.set("how have you been?")
label.pack()

img = Image.open('./images/tree/favicon.ico')
tkimg = ImageTk.PhotoImage(img)
image0 = tk.Label(down,image=tkimg)
image0.pack()


#Canvas
img1 = Image.open('./images/ball/6.jpg')
tk_img = ImageTk.PhotoImage(img1)

canvas = tk.Canvas(down,width=200)
canvas.create_image(0,0, anchor="center" ,image=tk_img)
canvas.pack()

down.mainloop()