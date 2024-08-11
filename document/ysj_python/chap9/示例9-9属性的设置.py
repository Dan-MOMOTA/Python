class Student:
    #首尾双下划线
    def __init__(self,name,gender):
        self.name=name #self._name受保护的，只能本类和子类访问
        self.__gender=gender #私有属性

    #使用@property修改方法，将方法转成属性使用
    @property
    def gender(self):
        return self.__gender
    
    #将我们的gender这个属性设置为可写属性
    @gender.setter
    def gender(self,value):
        if value != '男' and value != '女':
            print('性别有误,已将性别默认设置为男')
            self.__gender='男'
        else:
            self.__gender=value

stu=Student('陈梅梅','女')
print(stu.name,'的性别是：',stu.gender) #stu.gender就会去执行stu.gender()
#尝试修改属性值
#stu.gender='男' #AttributeError: property 'gender' of 'Student' object has no setter

stu.gender='其它' #赋值操作，调用第13行代码
print(stu.name,'的性别是:',stu.gender) #取值操作，调用第8行代码