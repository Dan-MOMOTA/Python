# 元素定位隐性等待
# 演示地址：https://bahuyun.com/bdp/form/1381564610060484609

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
a1.get("https://bahuyun.com/bdp/form/1381564610060484609")
# 元素定位隐性等待(多少秒内找到元素就立刻执行，没找到元素就报错)
a1.implicitly_wait(10) # 通用设置，针对a1的操作都会生效
a1.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[1]/i').click()