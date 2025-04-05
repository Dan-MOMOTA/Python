# 元素定位-CSS_SELECTOR

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

# 元素定位-CSS_SELECTOR
# 1.#id = 井号+id值 -> 通过id值来定位
a1.find_element(By.CSS_SELECTOR, '#kw').send_keys("bilibili0")
# 2..class = 点+class值 -> 通过class值来定位
a1.find_element(By.CSS_SELECTOR, '.s_ipt').send_keys("bilibili1")
# 3.不加修饰符 = 标签头 -> 通过标签头定位
a1.find_elements(By.CSS_SELECTOR, 'input')[7].send_keys("bilibili2")
# 4.通过任意类型定位:"[类型='精准值']"
a1.find_element(By.CSS_SELECTOR, "[autocomplete='off']").send_keys("bilibili3")
# 4.通过任意类型定位:"[类型*='模糊值']"
# 4.通过任意类型定位:"[类型^='开头值']"
# 4.通过任意类型定位:"[类型$='结尾值']"
# 以上这些方法都属于理论定位法

# 5.更简单的定位方式：在谷歌控制台直接复制 SELECTOR
# 缺点：各别元素定位值会特别长
a1.find_element(By.CSS_SELECTOR, "#kw").send_keys("bilibili4")