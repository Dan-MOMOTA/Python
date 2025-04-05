#设置浏览器
#禁用沙盒模式：add_argument('--no-sandbox')
#保持浏览器打开状态：add_experimental_option('detach'，True)
#创建并启动浏览器：webdriver.Chrome()

#导包：from selenium import webdriver
#导包：from selenium.webdriver.chrome.options import Options
#导包：from selenium.webdriver.chrome.service import Service

from selenium import webdriver  # 用于操作浏览器
from selenium.webdriver.chrome.options import Options  # 用于设置谷歌浏览器
from selenium.webdriver.chrome.service import Service  # 用于管理谷歌驱动

#创建设置浏览器对象
q1 = Options()
#禁用沙盒模式(增加兼容性问题)
q1.add_argument('--no-sandbox')
#保持浏览器打开状态(默认是代码执行完毕自动关闭)
q1.add_experimental_option('detach', True)

#创建并启动浏览器
a1 = webdriver.Chrome(service=Service('damaiAuto-master/chromedriver.exe'), options=q1)
