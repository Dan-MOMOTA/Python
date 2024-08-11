s='helloworld'
print('{0:*<20}'.format(s)) # 字符串的显示宽度为20，左对齐，空白部分使用* 号填充
print('{0:*>20}'.format(s))
print('{0:*^20}'.format(s))

# 居中对齐
print(s.center(20,'*'))

# 千位分隔符（只适用于整数和浮点数）
print('{0:,}'.format(987654321))
print('{0:,}'.format(987654321.7865))

# 浮点数小数部分的精度
print('{0:.2f}'.format(3.1419826))
# 字符串类型 .表示是最大的显示长度
print('{0:.5}'.format('helloworld')) # hello

# 整数类型
a=425
print('二进制:{0:b},十进制:{0:d},八进制:{0:o},十六进制:{0:x},十六进制：{0:X}'.format(a))

# 浮点数类型
b=3.1415926
print('{0:.2f},{0:.2E},{0:.2e},{0:.2%}'.format(b) )
