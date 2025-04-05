# 元素定位-LINK_TEXT

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

# 元素定位-LINK_TEXT
# 1.通过精准链接文本找到标签a的元素[精准文本定位]
# 2.有重复的文本需要切片处理
a1.find_element(By.LINK_TEXT, '新闻').click()