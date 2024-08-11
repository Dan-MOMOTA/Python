'''
实战一：使用面向对象思想实现乐器弹奏
需求：乐手可以弹奏不同的乐器从而发出不同的声音。可以弹奏的乐
器包括二胡、钢琴和琵琶。定义乐器类Instrument，包括方法
makesound(定义乐器类的子类：二胡Erhu、钢琴Piano和
小提琴Violin，定义一个函数可以弹奏各种乐器play(instrument），
测试给乐手不同的乐器让他弹奏。
'''

class Instrument(): #父类
    def make_sound(self):
        pass
    
class Erhu(Instrument):
    def make_sound(self):
        print('二胡在弹奏')
        
class Pinao(Instrument):
    def make_sound(self):
        print('钢琴在弹奏')
        
class Violin(Instrument):
    def make_sound(self):
        print('小提琴在弹奏')

#编写一个函数
def play(obj):
    obj.make_sound()

#测试
er=Erhu()
piano=Pinao()
vio=Violin()

#调用方法
play(er)
play(piano)
play(vio)