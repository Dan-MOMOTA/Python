def lower_upper(x): # x是一个字符串，形式参数
    lst=[]
    for item in x:
        if  'A'<=item<='Z':
           lst.append( chr(ord(item)+32)) # ord()将字母转成Unicode码整数 ，加上32， chr()整数码转成字符，
        elif 'a'<=item<='z':
            lst.append(chr(ord(item) - 32))
        else:
            lst.append(item)

    return ''.join(lst)

# 准备调用
s=input('请输入一个字符串')
new_s=lower_upper(s) # 函数的调用
print(new_s)

