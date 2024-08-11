lst=[54,56,77,4,567,34]
#(1)排序操作
asc_lst=sorted(lst) # 升序
desc_lst=sorted(lst,reverse=True) # 降序
print('原列表:',lst)
print('升序:',asc_lst)
print('降序:',desc_lst)

# （2）reversed 反向
new_lst=reversed(lst)
print(type(new_lst)) # <class 'list_reverseiterator'> 迭代器对象
print(list(new_lst))

#(3)zip
x=['a','b','c','d']
y=[10,20,30,40,50]
zipobj=zip(x,y)
print(type(zipobj)) # <class 'zip'>
#print(list(zipobj))

#(4)enumerate
enum=enumerate(y,start=1)
print(type(enum)) # <class 'enumerate'>
print(tuple(enum))

# (5)all
lst2=[10,20,'',30]
print(all(lst2)) #False  ,空字符串的布尔值是False
print(all(lst)) #True

#(6)any
print(any(lst2)) #True

#(7)
print(next(zipobj)) # ('a', 10)
print(next(zipobj))
print(next(zipobj))


def fun(num):
    return num%2==1 # 可能是True，False

obj=filter(fun,range(10))  # 将range(10),0-9的整数，都执行一次fun操作
print(list(obj)) # [1, 3, 5, 7, 9]

def upper(x):
    return x.upper()

new_lst2=['hello','world','python']
obj2=map(upper,new_lst2)
print(list(obj2))
