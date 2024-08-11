class Student:
    # 类属性：定义在类中，方法外的变量
    school='北京XXX教育'

    #初始方法
    def __init__(self,xm,age): #xm，age是方法的参数，是局部变量，xm，age的作用域是整个__init__方法
        self.name=xm #=左侧是实例属性，xm是局部变量，将局部变量的值xm赋值给实例属性self.name
        self.age=age #实例的名称和局部变量的名称可以相同