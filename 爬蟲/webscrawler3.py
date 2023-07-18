from bs4 import BeautifulSoup
import requests
import os

input_image = input("請輸入要下載的圖片")

response = requests.get(f"https://unsplash.com/s/photos/{input_image}")
soup = BeautifulSoup(response.text, "html.parser")

data = soup.find_all('div', {'class', "sBV1O"})

n = 0
for datal in data:
    n = n+1
    a = (datal.find('a')['href'])
           
    folder_path = f'./images/{input_image}/' #資料夾路徑
    img_name = folder_path +f"{n}.jpg" #檔案名稱命名規則制定
    r = requests.get(a) 
    os.makedirs(folder_path, exist_ok=True) #創建 folder_path 這個變數當中的資料路徑的資料夾，並且卻仁存在
    with open(img_name, 'wb') as f: # 打開檔案名(img_name)，透過二進制寫入(wb)，

        f.write(r.content) #寫入r讀到的所有資料(request.get(a))
        print('Dowlaad:' + img_name + '  ......')