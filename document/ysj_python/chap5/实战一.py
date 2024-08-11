lst=[88,89,90,98,00,99] # 表示的员工的两位整数出生年份
print(lst)
# 遍历列表的方式
# for index in range(len(lst)):
#     if str(lst[index])!='0':
#         lst[index]='19'+str(lst[index]) # 拼接年份，再赋值
#     else:
#         lst[index]='200'+str(lst[index])
#
# print('修改后的年份列表：',lst)

# 使用enumerate()函数
for index,value in enumerate(lst):
    if str(value) != '0':
        lst[index]='19'+str(value) # 拼接年份，再赋值
    else:
        lst[index]='200'+str(value)
print('修改后的年份列表：',lst)