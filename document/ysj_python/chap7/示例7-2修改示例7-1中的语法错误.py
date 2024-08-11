# 第一段代码
age=input('请输入你的年龄:')
if age>"18":
    print('成年人，做事需要负法律责任了！')

# 第二段代码
i=1
while i<10:
    print(i)
    i+=1

# 第三段代码
for i in range(3):
    uname=input('请输入用户名:')
    pwd=input('请输入密码:')
    if uname=='admin' and pwd=='admin':
        print('登录成功!')
        break
    else:
        print('输入有误！')
else:
    print('对不起，三次均输入错误')
