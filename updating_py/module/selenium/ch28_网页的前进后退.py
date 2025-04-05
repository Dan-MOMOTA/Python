# 网页前进后退

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
a1.get("https://baidu.com")

a1.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input').send_keys("bilibili")
a1.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[5]/div/div/form/span[2]/input').click()
time.sleep(1)
# 网页后退
a1.back()
time.sleep(1)
# 网页前进
a1.forward()