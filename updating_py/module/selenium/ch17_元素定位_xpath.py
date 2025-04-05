# 元素定位-XPATH

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

# 元素定位-XPATH
# 1.复制谷歌浏览器 Xpath (通过属性+路径定位,属性如果是随机的，可能定位不到)
a1.find_element(By.XPATH, '//*[@id="kw"]').send_keys("bilibili0")
# 2.复制谷歌浏览器 full Xpath 完整路径，缺点是定位值比较长，但是基本100%准确
a1.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[5]/div[2]/div/form/span[1]/input').send_keys("bilibili1")