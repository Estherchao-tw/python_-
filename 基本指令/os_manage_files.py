#python中非常重要的檔案管理套件，叫做os。它可以用來幫助你管理資料夾中的檔案，當然也可以做到一次更動檔名或資料的功能，

import os
#創建一個資料夾，利用os.mkdir這個指令，mkdir是MakeDictionaries的意思，顧名思義就是創建一個資料夾。


#os.mkdir('./test')


#after commanding 可以使用os.rmdir(RemoveDictionaries)來刪除指定資料夾。
#檔案管理套件，當然可以取得檔案的資料，就先從取得檔名開始講起，取得路徑下檔名非常的簡單，只要使用os.listdir就好了，例如我在剛剛的test資料夾中放了兩個檔案，a.txt跟b.txt，然後使用os.listdir:


list = os.listdir('./test')
print(list)
# 以串列(list) 形式顯示


# two way to open files
##　os.open  There are three parameters that can be placed in open, which are the file path, the reading and writing method, and the encoding method.

f = open("./test/a.txt", 'r',encoding='utf-8')
print(f.read())

f= open("./test/a.txt",'w',encoding='utf-8')
f.write("這是測試 w 的功能，更改檔案")
f.close() #檔案打開後，要close掉
x= open("./test/a.txt",'r',encoding='utf-8')
print(x.read())

f = open("./test/b.txt",'a',encoding='utf-8')
f.write("測試a 的功能，在文件後方輸入資料")
f.close()
y= open("./test/b.txt",'r',encoding='utf-8')
print(y.read())



