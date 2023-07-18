from bs4 import BeautifulSoup
import requests
import os

input_image = input("請輸入要下載的圖片")

response = requests.get(f"https://unsplash.com/s/photos/{input_image}")
soup = BeautifulSoup(response.text, "html.parser")

data = soup.find_all('div',{'class',"sBV1O"})
# print(data)

n= 0
for detail in data:
  n = n+1
  a = (detail.find('a')['href'])

  folder_path = f'./image/{input_image}/'
  img_name = folder_path + f"{n}.jpg"
  r = requests.get(a)
  os.makedirs(folder_path,exist_ok=True)
  with open(img_name,'wb') as f:
        f.write(r.content)
        print('Download:' + img_name + '  .......')

