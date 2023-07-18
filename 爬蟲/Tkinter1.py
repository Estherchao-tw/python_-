from tkinter import *
import tkinter  as tk 

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
down.mainloop()