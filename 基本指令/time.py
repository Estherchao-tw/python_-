import time
print(time.localtime())
# print(time.sleep()) 寫法錯誤，讓程式停止指定秒數，在各種領域都會用到。像在爬蟲中就會為了避免太頻繁對伺服器發送要求而讓每一次的發送請求都加入time.sleep()，避免被伺服器偵測。單位是秒。
print(time.time())

a= time.localtime()
print('今天是', a.tm_mon,"/",a.tm_mday)

# time.gmtime() 回傳世界utc時間 並非本地時間
# time.asctime() time.locaaltime()取出的時間轉成字串(list)的形式
print(time.asctime())



#time.strftime() 根據需求指定形式顯示
print(time.strftime("%Y / %m / %d %H:%M:%S", a))






