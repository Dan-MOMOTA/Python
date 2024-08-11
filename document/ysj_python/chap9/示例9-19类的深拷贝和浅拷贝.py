class CPU():
    pass

class Disk():
    pass

class Computer():
    #计算机出CPU和硬盘
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

cpu=CPU() #创建了一个CPU对象
disk=Disk() #创建了一个硬盘对象

#创建一个计算机对象
com=Computer(cpu,disk)
#变量(对象)的赋值
com1=com
print(com,'子对象的内存地址:',com.cpu,com.disk)
print(com1,'子对象的内存地址:',com1.cpu,com1.disk)

#类对象的浅拷贝
print('-'*40)
import copy
com2=copy.copy(com) #com2是新产生的对象，com2的子对象，cpu，disk不变
print(com,'子对象的内存地址:',com.cpu,com.disk)
print(com2,'子对象的内存地址:',com2.cpu,com2.disk)

#类对象的深拷贝
print('-'*40)
com3=copy.deepcopy(com) #com3是新产生的对象，com3的子对象，cpu，disk也会重写创建
print(com,'子对象的内存地址:',com.cpu,com.disk)
print(com3,'子对象的内存地址:',com3.cpu,com3.disk)