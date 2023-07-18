import random 
 
# Generate a random integer between 1 and 10 
random_number = random.randint(1, 10) 
print(random_number)
# 不能用random的檔案名!!

import random
print(random.randrange(1,11,3))# random choose from 1,4,7,10

#random.choice 從指定串列中抽出元素
import random
print(random.choice(['good morning','good evening','good night']))

#字串形式，會獨立字元(character)抽選
import random
print(random.choice("abcdefg"))


# random.choices 指定特定串列中抽出複數元素
# 常用參數K:指定取出的數量& weights: 指定取出的機率
import random 
a = ['good morning','good evening','good night']
print(random.choices(a,k=2))

#ｒａｎｄｏｍ．ｓａｍｐｌｅ　:從指定的字串(string)中取出特定數量的值，並以串列(list)形式回傳

import random
print(random.sample('abcdefg',3))

#random.shuffle() 打亂元素順序
import random
x = ['a','b','c']
random.shuffle(x)
print(x)














