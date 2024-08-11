# 倒三角形
# 1-->5 range(1,6) ,2-->4 range(1,5) 3-->3  range(1,4) ...    5-->1 range(1,2)
for i in range(1,6): # i表示的是行号，第i行
    for j in range(1,7-i):
        print('*',end='')
    print() # 内层循环执行完毕之后，空print()换行

print('------------------------------')
# 等腰三角形
'''
&&&&*
&&&***
&&*****
&*******
*********
'''
for i in range(1,6): # 外层循环 5行
    # 倒三角形
    for j in range(1,6-i):
        # print('&',end='')
        print(' ',end='')
    # 1,3,5,7...等腰三角形 range(1,2) ,range(1,4),range(1,6),  range(1,8),,,range(1,10)
    for k in range(1,i*2):
        print('*',end='')
    print() # 当两个并列的for循环执行完毕之后，再换行
