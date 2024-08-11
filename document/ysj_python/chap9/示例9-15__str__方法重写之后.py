class Person(object): #默认继承了object
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #方法重写
    def __str__(self):
        return '这是一个人类,具有name和age两个实例属性' #返回值是一个字符串

# 创建类的对象
per=Person('陈梅梅',20) #创建对象的时候会自动调用__init__方法
print(per) #还是内存地址吗？不是，__str__方法中的内容直接输出对象名，实际上是调用__str__方法
print(per.__str__())