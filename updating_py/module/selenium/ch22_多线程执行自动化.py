# 多线程执行自动化（四开浏览器）
# import threading

from selenium import webdriver  # 用于操作浏览器
from selenium.webdriver.chrome.options import Options  # 用于设置谷歌浏览器
from selenium.webdriver.chrome.service import Service  # 用于管理谷歌驱动
from selenium.webdriver.common.by import By
import time
import threading

class A1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set(self):
        q1 = Options()
        q1.add_argument('--no-sandbox')
        q1.add_experimental_option('detach', True)
        a1 = webdriver.Chrome(service=Service('damaiAuto-master/chromedriver.exe'), options=q1)
        a1.set_window_size(300, 400)
        a1.set_window_position(self.x, self.y)
        a1.implicitly_wait(10) # 通用设置，针对a1的操作都会生效 
        a1.get("https://bahuyun.com/bdp/form/1381564610060484609")
        return a1

    # 执行代码
    def excute(self):
        a1 = self.set()
        for x in range(3):
            a1.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[3]/div/div[2]/div/div/div[2]/div/i').click()
            a1.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[4]/div/div[2]/div/div/div[1]/span').click()
            a1.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[4]/div/div[2]/div/div/div[2]/span').click()
            a1.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div[5]/div/div[2]/div/div/div/select/option[2]').click()
            a1.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div[6]/div/div[2]/div/div/input').send_keys(2025040300)
            a1.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div[7]/div/div[2]/div/div[1]/div[2]/div[3]/i').click()
            a1.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div[7]/div/div[2]/div/div[2]/div[2]/div[5]/i[1]').click()
            a1.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div[8]/div/div[2]/div/div/div/div/div/input').send_keys(r"D:\Dan\3.Python\一些脚本\1.png") # 绝对路径

            a1.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div[1]/button').click()
            a1.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div[3]/button').click()

            a2 = a1.window_handles
            a1.close()
            a1.switch_to.window(a2[1])

s0 = A1(0, 0)
s1 = A1(800, 0)
s2 = A1(0, 400)
s3 = A1(800, 400)

threading.Thread(target=s0.excute).start()
threading.Thread(target=s1.excute).start()
threading.Thread(target=s2.excute).start()
threading.Thread(target=s3.excute).start()