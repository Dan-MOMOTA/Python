'''
实战一：定义一个圆的类计算面积和周长
需求：定义一个圆类一Circle，提供一个属性r(半径)，提供两个方法：
计算圆的面积get_area(self)和计算圆的周长get_perimeter(self)，
通过两个方法计算圆的周长和面积并且对计算结果进行输出，最后从键盘录入半径，
创建圆类的对象，并调用计算面积和周长的方法输出面积和周长。
'''

class Circle:
    def __init__(self,r):
        self.r=r 
    
    #计算面积的方法
    def get_area(self):
        #return3.14*self.r*self.r
        return 3.14*pow(self.r,2)
    
    #计算周长的方法
    def get_perimeter(self):
        return 2*3.14*self.r
    
#创建对象
r=eval(input('请输入圆的半径:'))
c=Circle(r)
#调用方法
area=c.get_area() #调用计算面积的方法
perimeter=c.get_perimeter() #调用计算周长的方法
print('圆的面积为:',area)
print('圆的周长为:',perimeter)