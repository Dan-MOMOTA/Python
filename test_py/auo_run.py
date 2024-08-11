import schedule
import time
#从Python标准库中的datetime模块中导入datetime类,在这个特定的情况下，这意味着你可以直接使用datetime类而无需在代码中使用datetime.datetime的完全限定名称。
from datetime import datetime

# Exercise1
def task():
    now = datetime.now()
    ctime = time.ctime()
    #print(now)
    today = datetime.today()
    #print(today)
    #格式化时间，格式参照time模块中的strftime方法
    ts = now.strftime("%Y-%m-%d %H:%M:%S")
    print(ts)
    print(ctime)
#task()

def task2():
    now = datetime.now()
    ts = now.strftime("%Y-%m-%d %H:%M:%S")
    print(ts + ' 666!')

def exercise1():
    # 清空任务
    schedule.clear()
    # 创建一个按3秒间隔执行任务
    schedule.every(3).seconds.do(task)
    # 创建一个按2秒间隔执行任务
    schedule.every(2).seconds.do(task2)
    while True:
        schedule.run_pending()

# Exercise2
def job():
    print("当前时间：", time.ctime(), "任务正在执行...")

#检查当前日期是否是每月的1号
def check_monthly():
    if datetime.now().day == 1:
        job()

def exercise2():
    # 每隔5秒运行一次job函数
    schedule.every(5).seconds.do(job)

    # 每隔1分钟运行一次job函数
    schedule.every(1).minutes.do(job)

    # 每天的10:30运行一次job函数
    schedule.every().day.at("10:30").do(job)

    # 每周一的10:30运行一次job函数
    schedule.every().monday.at("10:30").do(job)

    # 每月的1号的10:30运行一次job函数
    #schedule.every().month.at("10:30").do(job)


    # 每天运行一次check_monthly函数，检查是否是每月的1号
    schedule.every().day.at("00:00").do(check_monthly)

    # 运行已经计划好的任务
    while True:
        #程序会不断地检查是否有已经到达执行时间的任务，并执行它们
        schedule.run_pending()
        #让程序暂停执行一段时间，单位是秒。在这里，1 表示暂停的时间为1秒。
        time.sleep(1)

#当 Python 解释器运行一个脚本时，它会把当前模块的名称赋值给 __name__ 变量。
#如果当前模块是主程序（即直接执行的脚本），那么 __name__ 的值会被设置为 '__main__'。
#如果当前模块是被导入到其他模块中的，则 __name__ 的值就是模块的名称。
#当你在一个脚本中看到 if __name__ == '__main__': 这行代码时，
#它的意思是：“如果当前模块是主程序，则执行以下代码块”。
if __name__ == '__main__':
    #exercise1()
    exercise2()
# 使用示例：
# 运行此脚本后，每天上午9点会自动打印当前时间及提示信息