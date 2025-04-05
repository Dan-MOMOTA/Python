# 获取元素文本内容、是否可见
# 新闻网站：https://baijiahao.baidu.com/s?id=1828374171022777733&wfr=spider&for=pc

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
a1.get("https://baijiahao.baidu.com/s?id=1828374171022777733&wfr=spider&for=pc")

# 获取元素文本内容 text
a2 = a1.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/span').text
print(a2)

# 元素是否可见
a3 = a1.find_element(By.XPATH, '/html/body/svg').is_displayed
print(a3)