# 日期 评星 上传元素
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
    a1.implicitly_wait(10) # 通用设置，针对a1的操作都会生效 
    return a1

a1 = set()

# 打开指定网址
a1.get("https://bahuyun.com/bdp/form/1381564610060484609")

a1.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div[6]/div/div[2]/div/div/input').send_keys(2025040300)
a1.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div[7]/div/div[2]/div/div[1]/div[2]/div[3]/i').click()
a1.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div[7]/div/div[2]/div/div[2]/div[2]/div[5]/i[1]').click()
a1.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div[8]/div/div[2]/div/div/div/div/div/input').send_keys(r"D:\Dan\3.Python\一些脚本\1.png") # 绝对路径