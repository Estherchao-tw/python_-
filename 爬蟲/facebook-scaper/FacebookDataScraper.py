##
## 爬取臉書社團，在社團內部自動垂直瀏覽頁面，瀏覽頁面才能再入資料，爬取貼文，並把照片下載下來

from selenium import webdriver
from selenium.webdriver.chrome.service import Service #執行自動化測試或爬蟲任務，因為它可以模擬用戶的操作，同時可以訪問網頁上的信息。
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #鍵盤輸入的功能
from bs4 import BeautifulSoup
import numpy as numpy
import csv
import time
import os
import requests
###啟動瀏覽器

# webdriver.Chrome 用來連結webdriver，use webdriver.chrome open file'chromedriver.exe
#move the file 'chromedriver.exe' to the folder of the project，and remove the path from the code

#模擬用戶
service = Service(executable_path = "chromedriver")

# 阻擋通知
options = Options()
# options.add_argument("-disable-notifications") 

# pref 禁用瀏覽器彈出視窗
prefs = {"profile.default_content_setting_values.notifications":2}
options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(service=service,options=options)
driver.get('https://www.facebook.com/login')

email = driver.find_element(By.NAME,"email")
password = driver.find_element(By.NAME,"pass")
email.send_keys('xxxxxx@gmail.com')
password.send_keys('xxxx')

# time.sleep(2)
password.submit()

# 直接打開指定頁面
driver.get('https://www.facebook.com/TigerblueStory') ##sometimes it will break
# time.sleep(5)


### 爬取網頁資料並保存資料
# set var post as a list to preserve data 
for x in range(3):
  driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  print("scroll")
  time.sleep(3)



    # 使用 BeautifulSoup 解析網頁內容
    # Parse the page source with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

#每一行文字都是放在dir="auto"的<div>中。有空白可以留著不用打點
titles = soup.find_all('div',{'class': "xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a"})
# data = soup.find_all('div',{'class',"sBV1O"})

# print(titles)

for title in titles:
    #定位每一行標題
    posts = title.find_all('div',{'dir':"auto"})
    if len(posts) != 0:
      for post in posts:
        print(post.text)
    print("-"*30)

## 存貼文當中的照片
# #建立資料夾

data = soup.find_all('div',{'class',"x6ikm8r x10wlt62 x10l6tqk"})
# print(data)

# reference webscrawler2.py
n = 0
for detail in data:
  a = (detail.find('a')['href'])
  n = n+1
  folder_path = f'./image/'
  img_name = folder_path + f"{n}.jpg"
  r = requests.get(a)
  os.makedirs(folder_path,exist_ok=True)
  with open(img_name,'wb') as f:
        f.write(r.content)
        print('Download:' + img_name + '  .......')

# wait
time.sleep(5)
driver.close()
