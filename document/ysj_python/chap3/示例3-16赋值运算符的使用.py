x=20 # 直接赋值，直接将20赋值给左侧的变量x
y=10
x=x+y # 将x+y的和赋值给x ，x的值为30
print(x)  # x的值是30
x+=y   # 40  相当于x=x+y
x-=y # 相当于x=x-y
print(x) # 30
x*=y
print(x) # 300
x/=y
print(x) #30.0 发生了类型转换 x的数据类型为float类型
print(type(x)) # <class 'float'>
x%=2 # 相当于 x=x%2
print(x) # 0.0
z=3
y//=z  # 相当于y=y//z
print(y) # 3

y**=2 # 相当于 y=y**2
print(y)  # 9

# Python支持链式赋值
a=b=c=100 # 相当于执行 a=100 b=100  c=100
print(a,b,c)

# Python支持系列解包赋值
a,b=10,20  # 相当于执行了a=10  b=20
print(a,b)

print('-----如何交换两个变量的值呢?-----')
a,b=b,a # 将b的值赋给a,将a的值赋给b
print(a,b)

