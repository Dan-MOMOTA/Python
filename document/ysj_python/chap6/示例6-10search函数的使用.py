import re
pattern='\d\.\d+'
s='I study Python3.11 every day Python2.7 I love you'
match=re.search(pattern,s)

s2='4.10 Python I study every day'
s3='I study Python every day'

match2=re.search(pattern,s2)
match3=re.search(pattern,s3) # None
print(match)
print(match2)
print(match3)

print(match.group())
print(match2.group())