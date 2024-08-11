import random
rand=random.randint(1,100) # 产生1-100之间的随机数
count=1 # 记录猜数的次数
while count<=10:
    number=eval(input('在我心中有个数，1-100之间，请你猜一猜:'))
    if number==rand:
        print('猜对了')
        break
    elif number>rand:
        print('大了')
    else:
        print('小了')
    count+=1 # 每猜一次count次数要加1
# 判断次数
if count<=3:
    print('真聪明，一共猜了',count,'次')
elif count<=6:
    print('还可以，一共猜了',count,'次')
else:
    print('猜的次数有点多啊，一共猜了',count,'次')