print('绝对值:',abs(100),abs(-100),abs(0))
print('商和余数:',divmod(13,4))
print('最大值:',max('hello'))
print('最大值:',max([10,4,56,78,4]))
print('最小值:',min('hello'))
print('最小值:',min([10,4,56,78,4]))

print('求和:',sum([10,34,45]))
print('x的y次幂:',pow(2,3))

# 四舍五入
print(round(3.1415926)) # round函数只有一个参数，保留整数
print(round(3.9415926)) # 4
print(round(3.1415926,2)) # 2表示的是保留两位小数
print(round(314.15926,-1)) # 314 ,-1位，个位进行四舍五入

print(round(314.15926,-2)) #300 ,-2,十位进行四舍五入