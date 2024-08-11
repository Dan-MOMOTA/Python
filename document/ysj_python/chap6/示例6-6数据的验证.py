# isdigit()十进制的阿拉伯数字
print('123'.isdigit()) # True
print('一二三'.isdigit()) # False
print('0b1010'.isdigit()) # False
print('ⅢⅢⅢ'.isdigit()) # False
print('-'*50)
# 所有字符都是数字
print('123'.isnumeric()) # True
print('一二三'.isnumeric())# True
print('0b1010'.isnumeric()) # False
print('ⅢⅢⅢ'.isnumeric()) # True
print('壹贰叁'.isnumeric()) # True
print('-'*50)
# 所有字符都是字母(包含中文字符)
print('hello你好'.isalpha()) # True
print('hello你好123'.isalpha()) # False
print('hello你好一二三'.isalpha()) # True
print('hello你好ⅢⅢⅢ'.isalpha()) # False
print('hello你好壹贰叁'.isalpha()) # True
print('-'*50)
# 所有字符都是数字或字母
print('hello你好'.isalnum()) # True
print('hello你好123'.isalnum()) #True
print('hello你好一二三'.isalnum()) #True
print('hello你好ⅢⅢⅢ'.isalnum()) #True
print('hello你好壹贰叁'.isalpha()) # True

print('-'*50)
# 判断字符的大小写
print('HelloWorld'.islower()) # False
print('helloworld'.islower()) # True
print('hello你好'.islower()) # True

print('-'*50)
print('HelloWorld'.isupper()) # False
print('HELLOWORLD'.isupper()) # True
print('HELLO你好'.isupper()) # True
print('-'*50)
#所有字符都是首字母大写
print('Hello'.istitle()) # True
print('HelloWorld'.istitle()) # False
print('Helloworld'.istitle()) # True
print('Hello World'.istitle()) # True
print('Hello world'.istitle()) # False

# 判断是否都是空白字符
print('-'*50)
print('\t'.isspace()) # True
print(' '.isspace()) # True
print('\n'.isspace()) # True