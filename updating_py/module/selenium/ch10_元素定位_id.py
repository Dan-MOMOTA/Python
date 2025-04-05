# 元素定位-ID

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

# 1.通过id定位元素，一般比较准确；
# 2.并不是所有网页或者元素都有id值
a1.find_element(By.ID, 'kw').send_keys('bilibili')