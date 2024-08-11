# 直接使用[]创建列表
lst=['hello','world',98,100.5]
print(lst)

# 可以使用内置的函数list()创建列表
lst2=list('helloworld')
lst3=list(range(1,10,2)) # 从1开始到10结束，步长为2，不包含10
print(lst2)
print(lst3)

# 列表是序列中的一种，对序列的操作符，运算符，函数均可以使用
print(lst+lst2+lst3) # 序列中的相加操作
print(lst*3) # 序列的相乘操作
print(len(lst))
print(max(lst3))
print(min(lst3))

print(lst2.count('o')) # 统计o的个数
print(lst2.index('o')) # o在列表lst2中第一次出现的位置

# 列表的删除操作
lst4=[10,20,30]
print(lst4)
# 删除列表
del lst4
#print(lst4) # NameError: name 'lst4' is not defined. Did you mean: 'lst'?