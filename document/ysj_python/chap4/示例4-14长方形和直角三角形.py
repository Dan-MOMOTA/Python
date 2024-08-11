# 三行四列
for i in range(1,4): # 外层循环行
    for j in range(1,5): # 内层循环 列
        print('*',end='')
    print() # 空的print语句，作用是换行
print('-----------------')
for i in range(1,6): # 5行
    # *的个数与行相同,range(1,2),第二行，range(1,3)
    for j in range(1,i+1):
        print('*',end='')
    print() # 空的print语句，换行
