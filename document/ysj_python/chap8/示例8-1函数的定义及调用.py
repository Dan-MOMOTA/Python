def get_sum(num): #num叫形式参数
    s=0
    for i in range(1,num+1):
        s+=i
    print(f'1到{num}之间的累加和为:{s}')

# 函数的调用
get_sum(10) # 1-10之间的累加和     10是实际参数值
get_sum(100) # 1-100之间的累加和   100是实际参数值
get_sum(1000) # 1-1000之间的累加和  1000是实际参数值
