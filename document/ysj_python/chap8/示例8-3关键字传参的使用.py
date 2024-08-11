def happy_birthday(name,age):
    print('祝'+name+'生日快乐')
    print(str(age)+'岁生日快乐')

# 关键字传参
happy_birthday(age=18,name='娟子姐')

#happy_birthday(age=18,name1='娟子姐') # 定义的形参为name， TypeError: happy_birthday() got an unexpected keyword argument 'name1'

happy_birthday('陈梅梅',age=18) # 正常执行， 位置传参，也可以使用关键字传参

#happy_birthday(name='陈梅梅',18) # SyntaxError: positional argument follows keyword argument

# 位置传参在前，关键字传参在后