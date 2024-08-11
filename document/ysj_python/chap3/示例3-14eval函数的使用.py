s='3.14+3'
print(s,type(s))
x=eval(s) # 使用eval函数去掉s这个字符串中左右的引号 ,执行加法运算
print(x,type(x))

# eval函数经常与input()函数一起使用，用来获取用户输入的数值
age=eval(input('请输入您的年龄:')) # 将字符串类型转成了int类型，相当于int(age)
print(age,type(age))

height=eval(input('请输入您的身高:'))
print(height,type(height))

hello='北京欢迎你'
print(hello)
print(eval('hello')) # 输出了"北京欢迎你"
print(eval('北京欢迎你')) # NameError: name '北京欢迎你' is not defined
