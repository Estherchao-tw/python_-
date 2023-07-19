# from PIL import Image
from PIL import Image,ImageDraw,ImageFont
import os

input_image = input("想修改甚麼圖片") 
img = Image.open(f"./images/ball/{input_image}.jpg")
# img.show()

#旋轉90度
# newImg = img.rotate(90)

#模式轉換
# black or white [0,1]
# newImg = img.convert('1')
# black white gray
#newImg = img.convert('L')
# rgba
# newImg = img.convert("RGB")
#cmyk 印刷全彩
# newImg = img.convert("CMYK")

# 更改圖片尺寸(長寬)
# newImg = img.resize((500,1000),Image.LANCZOS)

#嵌字，在照片加上文字
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Candara.ttf",150)
color = "red"
text = "test message"

draw.text((50,10),text,fill=color,font=font)




# newImg.show(draw.text)

folder_path = f'./images/ball/revise/'
os.makedirs(folder_path,exist_ok=True)
img_name = folder_path + f"draw_{input_image}.jpg"
# newImg.save(img_name)
img.save(img_name)

# newImg.save(img_name,"jpg")
