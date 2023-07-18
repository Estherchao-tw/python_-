# tuple is simiar to list ，tuple不能修改，而且定義時要用()，取出時用[]
week = ("Monday","Tusday","Wednesday")
print(week[1])

# dict={key:value}

dict = { "date":"20220710","time":"0335","week":"Tueday"}
del dict["date"]
dict["Weather"] = "Sun"
print(dict["Weather"])
print(len(week))
print(len(dict))

