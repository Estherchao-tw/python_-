#合成照片
from PIL import Image
import os

input_imageA = input("想修改甚麼圖片") 
imageA = Image.open(f"./images/ball/{input_imageA}.jpg")

input_imageB = input("想修改甚麼圖片") 
imageB = Image.open(f"./images/ball/{input_imageB}.jpg")
imageB = imageB.convert("RGBA")
widthB , heightB = imageB.size

newimageB  = imageB.resize((int(widthB*0.2),int(heightB*0.2)),Image.LANCZOS)

resultPicture = Image.new('RGBA', imageA.size, (0, 0, 0, 0))

resultPicture.paste(imageA,(0,0))
resultPicture.paste(newimageB, (0,0), newimageB)


folder_path = f'./images/ball/revise/'
os.makedirs(folder_path,exist_ok=True)
img_name = folder_path + f"con_{input_imageA}+{input_imageB}.png"
resultPicture.save(img_name)