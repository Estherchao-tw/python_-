# 大小寫
a = 'a B cD eF'
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())


b = 'abcdef'
print(b.isupper())
print(b.islower())



#字串分割
a = 'This is a banana.'
b = 'This/is/a/banana.'
print (a.split())
print (b.split('/',2))

# 字串格式化:想要在字串內回傳變數的直，要用f 字串。 用法是在字串前加入f ，並在回傳直前加大括弧{}
a = 10
print(f"I　have {a} bananas")


#使用者輸入：　用於系統跟使用者互動，讓使用者輸入資料
a = input("請輸入")
print(a)
