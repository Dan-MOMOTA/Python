
def get_find(s,lst):
    for item in lst:
        if s ==item:
            return True
    return False
lst=['hello','world','python']
s=input('请输入您要判断的字符串:')
result=get_find(s,lst)
print('存在' if result else '不存在') # if..else的简写，三元运算符  if result==True  if result 利用到对象的布尔值
