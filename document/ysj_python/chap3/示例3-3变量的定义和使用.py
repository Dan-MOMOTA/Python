luck_number=8  # 创建一个整型变量luck_number,并为其赋值为8

my_name ='杨淑娟' # 字符串类型的变量

print('luck_number的数据类型是:',type(luck_number)) # <class 'int'>
print(my_name,'的幸运数字是:',luck_number)

# Python动态修改变量的数据类型，通过赋不同类型的值就可以直接修改
luck_number='北京欢迎你'
print('luck_number的数据类型是:',type(luck_number)) # <class 'str'>

# 在Python中允许多个变量指向同一个值
no=number=1024  # no与number都指向了1024这个整数值
print(no,number)
print(id(no)) # id()查看对象的内存地址的 2535525366736
print(id(number)) # 2535525366736