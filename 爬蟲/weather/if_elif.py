a = 2
b = 3
if a<b:
    print('a<b')      # a<b
    if a==1:
        print('a=1')  # 不會印出
    elif a==2:
        print('a=2')  # a=2
    else a==2:
        print('a=3')  # 不會印出
elif a>b:
    print('a>b')      # 不會印出
else:
    print('a=b')      # 不會印出
print('ok')           # ok