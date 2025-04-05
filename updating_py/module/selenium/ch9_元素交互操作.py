# 元素交互操作
# 元素点击
# 元素输入
# 元素清空

from selenium import webdriver  # 用于操作浏览器
from selenium.webdriver.chrome.options import Options  # 用于设置谷歌浏览器
from selenium.webdriver.chrome.service import Service  # 用于管理谷歌驱动
from selenium.webdriver.common.by import By
import time

# 设置浏览器、启动浏览器
def set():
    q1 = Options()
    q1.add_argument('--no-sandbox')
    q1.add_experimental_option('detach', True)
    a1 = webdriver.Chrome(service=Service('damaiAuto-master/chromedriver.exe'), options=q1)
    return a1

a1 = set()

# 打开指定网址
a1.get("https://baidu.com/")

# 定位一个元素(找到的话返回结果，找不到的话报错)
a2 = a1.find_element(By.ID, 'kw')

# 元素输入
a2.send_keys("bilibili")
time.sleep(3)
# 元素清空
a2.clear()
time.sleep(3)
a2.send_keys("bilibili")
time.sleep(3)
# 找到按钮
a2 = a1.find_element(By.ID, 'su')
# 元素点击
a2.click()