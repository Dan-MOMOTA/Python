class Person: #默认继承了object
    def __init__(self,name,age):
        self.name=name 
        self.age=age

    def show(self):
        print(f'大家好,我叫:{self.name},我今年:{self.age}岁')

# Student继承Person类
class Student(Person):
    #编写初始化的方法
    def __init__(self,name,age,stuno):
        super().__init__(name,age) #调用父类的初始化方法
        self.stuno=stuno
    
    def show(self):
        #调用父类的方法
        super().show()
        print(f'我来自xxx大学,我的学号是:{self.stuno}')

# Doctor继承Person类
class Doctor (Person):
    #编写初始化方法
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department=department

    def show(self):
        #super().show() #调用父类的show方法
        print(f'大家好,我叫:{self.name},我今年:{self.age}岁,我的工作室是:{self.department}')

# 创建第一个子类对象
stu=Student('陈梅梅',20,'1001')
stu.show() #调用子类自己的show方法

doctor=Doctor('张一一',32,'外科')
doctor.show() #调用子类自己的show方法