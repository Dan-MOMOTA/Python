'''
实战一：定义学生类录入5个学生信息存储到列表中
需求：定义学生类Student，包含姓名，年龄，性别，分数四个属性，
提供一个用于学员信息输出的方法info（self)。编写测试代码，使用
循环录入5位学生的信息，由于录入的学生信息中间使用“#”进行分隔，
所以需要使用字符串的splitO方法，进行劈分，使用劈分的信息创建
学生对象，使用列表存储学生信息，最后使用循环遍历列表，调用对
象的info（方法输出学员信息。
'''

class Student:
    def __init__(self,name,age,gender,score):
        self.name=name
        self.age=age
        self.gender=gender
        self.score=score
    #实例方法
    def info(self):
        print(self.name,self.age,self.gender,self.score)

print('请输入5位学生信息:(姓名#年龄#性别#成绩)')
lst=[] #用于存储5个学生对象
for i in range(1,6):
    s=input(f'请输入第{i}位学生信息及成绩')
    s_lst=s.split('#') #索引为0的是姓名，索引为1的是年龄，索引为2的是性别，索引为3的是成绩
    # 创建学生对象
    stu=Student(s_lst[0],s_lst[1],s_lst[2],s_lst[3])
    #将学生对象添加到列表中
    lst.append(stu)

#遍历列表，调用学生对象的info方法
for item in lst: #item的数据类型是Student类型
    item.info()#对象名.方法名()