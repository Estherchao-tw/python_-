import os 
a = "../maxine/侖新科技/精密儀器室"
files = os.listdir(a)
g = len(a)
print(g)

for i in range(0,g):
  os.rename(f"../maxine/侖新科技/精密儀器室/{files[i]}",f"../maxine/侖新科技/有機/{i}.jpg")

#將路徑存到ａ　變數當中，透過os.listdir 將a 當中所有檔案存到files，利用變數讀取a 裡面有多少檔案，也可以使用讀取files讀出檔案數量
#更換檔案名，從0開始到g ，一個一個檔案批次更改，更改後的檔案放在另外一個檔案家中，檔案名稱隨著i 變動













