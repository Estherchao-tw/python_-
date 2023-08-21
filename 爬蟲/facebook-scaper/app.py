#自動登入臉書，進入查詢跟印出每篇貼文的第一段話

from selenium import webdriver
from selenium.webdriver.chrome.service import Service #執行自動化測試或爬蟲任務，因為它可以模擬用戶的操作，同時可以訪問網頁上的信息。
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #鍵盤輸入的功能
import time
from bs4 import BeautifulSoup


# webdriver.Chrome 用來連結webdriver，use webdriver.chrome open file'chromedriver.exe
#move the file 'chromedriver.exe' to the folder of the project，and remove the path from the code

service = Service(executable_path = "chromedriver")

options = Options()
options.add_argument("-disable-notifications")
driver = webdriver.Chrome(service=service,options=options)
driver.get('https://www.facebook.com/login')

email = driver.find_element(By.NAME,"email")
password = driver.find_element(By.NAME,"pass")
email.send_keys('xxxx@gmail.com')
password.send_keys('xxxxxx')

password.submit()

## By.CLASS_NAME TRY UPPER LETTER
search = driver.find_element(By.CLASS_NAME,"x1i10hfl.xggy1nq.x1s07b3s.x1kdt53j.x1yc453h.xhb22t3.xb5gni.xcj1dhv.x2s2ed0.xq33zhf.xjyslct.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.xnwf7zb.x40j3uw.x1s7lred.x15gyhx8.x9f619.xzsf02u.xdl72j9.x1iyjqo2.xs83m0k.xjb2p0i.x6prxxf.xeuugli.x1a2a7pz.x1n2onr6.x15h3p50.xm7lytj.x1sxyh0.xdvlbce.xurb0ha.x1vqgdyp.x1xtgk1k.x17hph69.xo6swyp.x1ad04t7.x1glnyev.x1ix68h3.x19gujb8")

#輸入文字後webdriver就會將我輸入的文字輸入到facebook的查詢功能。
searchWord= input("請輸入關鍵字")
search.send_keys(searchWord)
time.sleep(.5)
search.send_keys(Keys.ENTER)

time.sleep(3)

#其實這樣網頁還不算加載完成，因為在網頁沒有向下捲動時，其他的文章式不會加載進來的，所以我們需要讓webdriver做向下滾動的功能，這邊可以使用一個小迴圈:

for x in range(1,3):
  driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  time.sleep(5)

soup = BeautifulSoup(driver.page_source,'html.parser')

titles = soup.find_all('div',{'class':"xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a"})
# print('\n'.join('{}: {}'.format(*k) for k in enumerate(titles) ))

post = {index : title.find('div',{'dir':"auto"}).getText() for index,title in enumerate(titles)}
print(post)

driver.quit()