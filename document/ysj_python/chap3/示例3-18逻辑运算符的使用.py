print(True and True)
print(True and False)
print(False and False)
print(False and True)
print('-'*40)

print(8>7 and 6>5) # True
print(8>7 and 6<5)  # False
print(8<7 and 10/0) # False ,10/0并没有运算，当第一个表达式的结果为False，直接得结果，不会计算 and右侧的表达式了

print('-'*40)
print(True or True)
print(True or False)
print(False or False)  # False
print (False or True)

print('-'*40)
print(8>7 or 10/0) # True ，左侧的表达式结果为True时，or的右侧表达式根本不执行运算符
print('-'*40)
print( not True ) # False
print( not False) # True
print( not (8>7) ) # False