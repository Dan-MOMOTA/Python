# 元素定位-CLASS_NAME

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
a1.get("https://www.bilibili.com/")

# 元素定位-CLASS_NAME
# 1.class值不能有空格，否则会报错
#a1.find_element(By.CLASS_NAME, 'bg s_btn').click() # 会报error，因为有空格
# 2.class值重复的话需要切片操作，要使用find_elements！！！
# 3.class的值有些网站会是随机的---防止别人自动化
a1.find_elements(By.CLASS_NAME, 'channel-link')[5].click()