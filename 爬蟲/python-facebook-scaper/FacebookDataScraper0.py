from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
def get_facebook_post_count(page_url):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode

    # Path to your ChromeDriver executable
    # webdriver_path = '/path/to/chromedriver'

    # Create a new ChromeDriver service
    # service = Service(webdriver_path)
    service = Service(executable_path = "chromedriver")
    # 使用 Selenium 啟動瀏覽器
    # Start the WebDriver service
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 加載 Facebook 頁面
    # Facebook page URL
    facebook_page_url = 'https://www.facebook.com/TigerblueStor'

    # Navigate to the Facebook page
    driver.get(facebook_page_url)

    # Wait for the page to load，等待頁面完全加載
    driver.implicitly_wait(10)

    # Get the page source
    page_source = driver.page_source

    # Close the WebDriver
    # 關閉瀏覽器
    driver.quit()

    # 使用 BeautifulSoup 解析網頁內容
    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the elements containing the posts
    post_elements = soup.find_all('div', {'class': 'userContentWrapper'})

      # 尋找包含貼文數目的元素
      post_count_element = soup.find('span', {'class': 'post_count'})

      if post_count_element:
          # 獲取貼文數目的文字內容
          post_count_text = post_count_element.text
          # 解析文字內容中的數字
          post_count = int(post_count_text.replace(',', ''))
          return post_count
      else:
          return 0

    # 輸入要爬取的 Facebook 頁面的 URL
    facebook_page_url = 'https://www.facebook.com/example_page'

    # 獲取貼文數目總和
    total_post_count = get_facebook_post_count(facebook_page_url)

    print('Total post count:', total_post_count)

