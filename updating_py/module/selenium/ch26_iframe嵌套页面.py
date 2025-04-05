# iframe嵌套页面进入、退出
# 演示地址：https://sahitest.com/demo/iframesTest.htm

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
a1.get("https://sahitest.com/demo/iframesTest.htm")

# 获取iframe元素
a2 = a1.find_element(By.XPATH, '/html/body/iframe')

# iframe标签头说明当前嵌套了网页
# 进入iframe嵌套页面
a1.switch_to.frame(a2)

# 进入iframe嵌套页面点击
a1.find_element(By.XPATH, '/html/body/table/tbody/tr/td[1]/a[1]').click()

# 退出iframe嵌套页面(返回到默认页面)
a1.switch_to.default_content()
a1.find_element(By.XPATH, '/html/body/input[2]').click()
