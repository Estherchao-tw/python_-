# Selenium + Beautiful Soup: Facebook logging and scrapy

\#結合Python的Selenium及BeautifulSoup套件實現動態登入的網頁爬蟲

### 前情提要

**Beautiful Soup** 是網路爬蟲的一種方法。是一個用於從 HTML 和 XML 文件中提取數據的 Python 庫。它可以用"html parser"或是"xml parser"的解析器配合使用，提供你方便的訪問(網站)的方式。

所謂API 就是讓我們可以串接其他網站，並利用其他網站的資料來進行分析或其他運用，我們透過API串接其他網站，要調用API的某部分資料就需要requests,endpoints or subroitines.但我通常是用requests module。那取得其他網站的API，可以透過網站所提供的openAPI ，也可以用**Python 爬蟲**，將HTML解析下來分析你要的資訊。 

*hint: a program or programmer that uses one of these parts is said to call that portion of the API

**Selenium** 是自動化測試的一種方法。package Selenium 當中的 Webdriver，透過原生瀏覽器支援或瀏覽器擴充來直接控制瀏覽器。Webdriver 是針對各個瀏覽器而開發的，取代了嵌入被偵測web應用中的Python。Webdriver 還可以立永作業系統級的呼叫，**模擬使用者輸入**。來實現開啟頁面、進行登入，滑鼠模擬、執行javascripts程式。

這次就來實現兩個套件的結合運用，透過Selenium 載入動態網站，Beautiful Soup 可以輕鬆爬取想要的內容。自動登入臉書，進入查詢跟印出查詢後每篇貼文的第一段話。

Let's dive into this markdown!

------

### environment

pythin 3.8

selenium 4.10

beautifulsoup 4.12.2

------

### learning skill

- Selenium
  - 開啟瀏覽器:webdriver.chrome()
    - 警告框禁止處理 Option
  - 定位元素 By
  - 鍵盤操作 send_keys()
  - 網頁向下捲動 window.scrollTo()
  - 關視窗 driver.quit()
- Beautiful
  - Beautiful 解析網站
  - 取得元素 find_all()
  - 元素內文字 getText()

-----

#### 開啟瀏覽器:webdriver.chrome()

執行自動化測試或爬蟲任務，因為它可以模擬用戶的操作，同時可以訪問網頁上的信息。

```python
from selenium import webdriver

from selenium.webdriver.chrome.service import Service 
```

到官網去下載 chromdriver.exe

webdriver.Chrome 用來連結webdriver，use webdriver.chrome open file'chromedriver.exe

move the file 'chromedriver.exe' to the folder of the project，and remove the path from the code

```python
service = Service(executable_path = "chromedriver")
```

「瀏覽器驅動程式路徑」: "chromedriver"

#### 警告框禁止處理 Option

「瀏覽器設定(chrome_options)」: 彈出的視窗禁止

```python
service = Service(*executable_path* = "chromedriver")

options = Options()

options.add_argument("-disable-notifications")

driver = webdriver.Chrome(*service*=service,*options*=options)

driver.get('https://www.facebook.com/login')
```

就可以透過get()方法，前往要爬取的facebook 的網址。

## 定位元素 By

find_element_by_name 已經除去了，更新後selenium4.6需要新增

```python
from selenium.webdriver.common.by import By find_element(By.NAME,"name") 
```

透過By 宣告定位，並且傳入對應定位方法的定位參數

find_element() 方法只用於定位元素，他需要兩個參數。第一個參數式定位的型態，由By提供，可以到官網doc去看；第二個參數式定位的值。

**登入**: 需要的email and password就可以透過這個方法找到位置

*找到name ="email" and name = "pass"*

```python
email = driver.find_element(By.NAME,"email")
password = driver.find_element(By.NAME,"pass")
```

**搜尋**:需要的是那個輸入框的位置，可 以找到class

<img src="C:\Users\xperi\AppData\Roaming\Typora\typora-user-images\image-20230821174950380.png" alt="image-20230821174950380" style="zoom:50%;" />

#### 鍵盤操作 send_keys()

1. clear() : 清除文字
2. send_keys(value): 模擬按鍵輸入
3. click : 點擊元素
4. submit : 傳送表單

剛剛的帳號密碼可以用鍵盤操作方法輸入，搜索關鍵字的方法也是用這個方法傳送出去。

有些搜索框不提供搜索按鈕，而是透過按鍵盤上的ENTER 完成搜 所內容的傳送，這時也可以透過SUBMIT()

```python
# 登入網站
email.send_keys('xxxxx@gmail.com')

password.send_keys('xxxxxx')

password.submit()
```

ENTER 的方法我也嘗試過，在搜尋關鍵字當中實現:

在使用鍵盤按鍵方法前需要先匯入Keys 類別。

```python
#鍵盤輸入的功能
from selenium.webdriver.common.keys import Keys 
```

```python
# 搜尋關鍵字
# 輸入文字後webdriver就會將我輸入的文字輸入到facebook的查詢功能。
searchWord= input("請輸入關鍵字")

search.send_keys(searchWord)

time.sleep(.5)

search.send_keys(Keys.ENTER)
```

#### 網頁向下捲動 window.scrollTo()

進入查詢跟後，其實不能有效率抓取每篇貼文，也就是這樣網頁還不算加載完成，因為在網頁沒有向下捲動時，其他的文章式不會加載進來的，所以我們需要讓webdriver做向下滾動的功能，這邊可以使用一個小迴圈:

```
for x in range(1,3):

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

 time.sleep(5)
```

依照要項下滑的次數去更改 range 的範圍。

接下來要進入爬蟲~~

#### Beautiful 解析網站

網頁的HTML程式碼是從webdriver 來的，我們要使用diver.page_source 得到整篇程式碼。

接著BeautifulSoup類別(Class)，傳入取回的HTML結構字串，並且指定HTML parser來建立其物件，

```python
soup = BeautifulSoup(driver.page_source,'html.parser')
```

#### 取得元素 find_all()

使用BeautifulSoup套件的find_all()方法，取得每篇貼文的元素，也就是樣式類別(class)為xdj266r x11i5rnm...的所有<div>標籤，：

```python
titles = soup.find_all('div',{'class':"xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a"})

```

<img src="C:\Users\xperi\AppData\Roaming\Typora\typora-user-images\image-20230821181951904.png" alt="image-20230821181951904" style="zoom:50%;" />

#### 元素內文字 getText()

我們要的是上一步驟裡面的第一個div，利用Python迴圈讀取每一個文章標題的元素，透過BeautifulSoup套件的getText()方法，取得所有<div>標籤中的文字，我透過set 集合去跑迴圈，看起來簡潔多了

```python
post = {index : title.find('div',{'dir':"auto"}).getText() for index,title in enumerate(titles)}
print(post)
```

output:

![image-20230821182137957](C:\Users\xperi\AppData\Roaming\Typora\typora-user-images\image-20230821182137957.png)

#### 關視窗

最後，要記得關視窗

```python
driver.quit()
```

## error and method

error: This version of ChromeDriver only supports Chrome version 114 Current browser version is 116.0.5845.96

method : you just download the latest driver from seleniun

link: https://googlechromelabs.github.io/chrome-for-testing/

附上demo影片:



另外，facebookDataScraper.py ，製作自動化登入，並導向特定粉絲頁網站，存取貼文的照片。

you can check  facebook-scraper file, there is an .zip that contain all pictures from this program.

you can check the program from here : 