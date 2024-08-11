class Student:
    # 类属性：定义在类中，方法外的变量
    school='北京XXX教育'

    #初始方法
    def __init__(self,xm,age): #xm，age是方法的参数，是局部变量，xm，age的作用域是整个__init__方法
        self.name=xm #=左侧是实例属性，xm是局部变量，将局部变量的值xm赋值给实例属性self.name
        self.age=age #实例的名称和局部变量的名称可以相同

    #定义在类中的函数，称为方法，自带一个参数self
    def show(self):
        print(f'我叫：{self.name}, 今年{self.age}岁了')

#根据"图纸"可以创建N多个对象
stu1=Student('ysj',18)
stu2=Student('cmm',21)
print(stu1.name,stu1.age)
print(stu2.name,stu2.age)

#为stu2动态绑定一个实例属性
stu2.gender='男'
print(stu2.name,stu2.age,stu2.gender)

#print(stu1.gender)#AttributeError: 'Student' object has no attribute 'gender'

#动态绑定方法
def introduce():
    print('我是一个普通的函数，我被动态绑定完成了stu2对象的方法')
stu2.fun=introduce #函数的一个赋值
#fun就是stu2对象的方法
#调用
stu2.fun()
