s=0 # 存储累加和
i=1   #(1)初始化变量
while i<11:  #(2)条件判断
    # (3)语句块
    s+=i
    if s>20:
        print('累加和大于20的当前数是:',i)
        break
    i+=1 # (4)改变变量

print('--------------------------')
i=0 # 统计登录的次数 (1)初始化变量
while i<3:  #(2)条件判断
    # (3)语句块
    user_name=input('请输入用户名:')
    pwd=input('请输入密码:')
    if user_name=='ysj' and pwd=='888888':
        print('系统正在登录，请稍后...')
        break
    else:
        if i<2:
            print('用户名或密码不正确,您还有',2-i,'次机会')
    # (4)改变变量
    i+=1
else: # while...else
    print('三次均输入错误！')


