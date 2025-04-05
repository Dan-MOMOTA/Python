# 元素定位-TAG_NAME

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
a1.get("https://www.baidu.com/")

# 元素定位-TAG_NAME
# 1.找出<开头标签名字>
# 2.重复的标签名字特别多，需要切片
a1.find_elements(By.TAG_NAME, 'input')[7].send_keys("bilibili")