class Person: #默认继承了object
    def __init__(self,name,age):
        self.name=name 
        self.age=age

    def show(self):
        print(f'大家好，我叫：{self.name}，我今年：{self.age}岁')

# Student继承Person类
class Student(Person):
    #编写初始化的方法
    def __init__(self,name,age,stuno):
        super().__init__(name,age) #调用父类的初始化方法
        self.stuno=stuno

# Doctor继承Person类
class Doctor (Person):
    #编写初始化方法
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department=department

# 创建第一个子类对象
stu=Student('陈梅梅',20,'1001')
stu.show()

doctor=Doctor('张一一',32,'外科')
doctor.show()