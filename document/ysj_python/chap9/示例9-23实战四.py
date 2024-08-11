'''
实战一：使用面向对象思想设计自定义类，描述出租车和家用轿车的信息
需求：
出租车类：
    属性包括：车型，车牌，所属出租公司；方法包括：启动，停止
家用轿车类：
    属性包括：车型，车牌，车主姓名；方法包括：启动，停止
'''

class Car(object):
    def __init__(self,type,no):
        self.type=type
        self.no=no

    def start(self):
        print('我是车，我能启动')
    def stop(self):
        print('我是车，我可以停止')
        
#出租车
class Taxi(Car):
    def __init__(self,type,no,company):
        super().__init__(type,no)
        self.company=company
    #重写父类的启动和停止的方法
    def start(self):
        print('乘客您好！')
        print(f'我是{self.company}出租车公司，我的车牌时：{self.no}，您要去哪里？')
        
    def stop(self):
        print('目的地到了，请您扫码付款，欢迎下次乘坐')

#家用轿车
class FamilyCar(Car):
    def __init__(self,type,no,name):
        super().__init__(type,no)
        self.name=name
        
    def start(self):
        print(f'我是{self.name},我的轿车我做主')
            
    def stop(self):
        print('目的地到了，我们去玩儿吧！')

#测试
taix=Taxi('上海大众','京A88888','长城')
taix.start()
taix.stop()
print('-'*40)
family_car=FamilyCar('广汽丰田','京B66666','武大郎')
family_car.start()
family_car.stop()