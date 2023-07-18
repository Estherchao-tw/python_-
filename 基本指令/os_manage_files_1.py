import os
path = os.getcwd() # 得到當前路徑
print(path)

# os.rename:更改檔案名 
#os.rename('test/a.txt','test/abc.txt')
#os.remove :刪除檔案
os.remove('test/b.txt')

# os.rmdir:刪除檔案夾(需要是空目錄)
os.rmdir('test')




