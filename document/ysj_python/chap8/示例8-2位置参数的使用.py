def happy_birthday(name,age):
    print('祝'+name+'生日快乐')
    print(str(age)+'岁生日快乐')

# 调用
#happy_birthday('娟子姐') # TypeError: happy_birthday() missing 1 required positional argument: 'age'

#happy_birthday(18,'娟子姐') # TypeError: can only concatenate str (not "int") to str
# 正确的调用方式
happy_birthday('娟子姐',18)