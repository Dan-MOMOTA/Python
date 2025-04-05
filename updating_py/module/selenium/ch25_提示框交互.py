# 提示框（alert）元素交互
# 演示地址：https://sahitest.com/demo/promptTest.htm
# 弹窗输入内容
# 点击弹窗确定按钮

from selenium import webdriver  # 用于操作浏览器
from selenium.webdriver.chrome.options import Options  # 用于设置谷歌浏览器
from selenium.webdriver.chrome.service import Service  # 用于管理谷歌驱动
from selenium.webdriver.common.by import By
import time

def set():
    q1 = Options()
    q1.add_argument('--no-sandbox')
    q1.add_experimental_option('detach', True)
    a1 = webdriver.Chrome(service=Service('damaiAuto-master/chromedriver.exe'), options=q1)
    a1.implicitly_wait(10) # 通用设置，针对a1的操作都会生效 
    return a1

a1 = set()
a1.get("https://sahitest.com/demo/promptTest.htm")

a1.find_element(By.XPATH, '/html/body/form/input[1]').click()

# 弹窗输入内容
a1.switch_to.alert.send_keys("hhhhhhhhh")

# 点击弹窗确定按钮
a1.switch_to.alert.accept()