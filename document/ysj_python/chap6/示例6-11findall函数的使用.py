import re # 导入
pattern='\d\.\d+' # +限定符，\d 0-9数字出现1次或多次
s='I study Python3.11 every day Python2.7 I love you'
s2='4.10 Python I study every day'
s3='I study Python every day'
lst=re.findall(pattern,s)
lst2=re.findall(pattern,s2)
lst3=re.findall(pattern,s3)

print(lst)
print(lst2)
print(lst3)
