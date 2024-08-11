"""
基于python和selenium实现的大麦网自动刷新抢票脚本
用户要提前添加好个人信息和收货地址
"""

from selenium import webdriver #用于控制浏览器
from selenium.webdriver.support.ui import WebDriverWait #用于等待页面元素加载完成
from selenium.webdriver.common.keys import Keys #用于模拟键盘操作
from selenium.webdriver.common.by import By #用于定义查找页面元素的方式
from selenium.webdriver.support import expected_conditions as EC #用于等待页面元素加载完成
from selenium.common.exceptions import TimeoutException #用于处理当WebDriver在等待某个条件成立时，如果在指定的时间内条件没有成立时抛出的异常
import time

# 设置抢票链接和开票时间

URL = "https://detail.damai.cn/item.htm?spm=a2oeg.search_category.0.0.43d34d15C4SH4w&id=783142111836&clicktitle=Fall%20Out%20Boy%E6%BC%94%E5%94%B1%E4%BC%9A2024-fall%20out%20boy%E6%89%93%E5%80%92%E7%94%B7%E5%AD%A9%2F%E7%BF%BB%E9%97%B9%E5%B0%8F%E5%AD%90-%E5%8C%97%E4%BA%AC%E7%AB%99"# PC页面
#URL = 'http://m.damai.cn/damai/perform/item.html?projectId=146290'#手机页面
HOUR = 19
MIN  = 0
USERNAME = "13112390306"

#创建了一个Chrome浏览器实例
driver = webdriver.Chrome()
# 第一个参数driver是你之前创建的WebDriver实例，它控制着浏览器的行为。
# 第二个参数5是一个时间参数，表示WebDriverWait会等待最多5秒，直到所期望的条件成立。如果条件在5秒内没有成立，将会抛出TimeoutException异常。
wait = WebDriverWait(driver, 5)
#让WebDriver控制的浏览器打开指定的URL地址
driver.get(URL)

"""
PC端网页抢票操作
"""
#在页面上找到一个可点击的元素，并在该元素准备好被点击时返回该元素
def choose(seletor):
    try:
        # 控件可点击时才选定
        choice = wait.until(EC.element_to_be_clickable((By.XPATH, seletor)))
        return choice
    except TimeoutException as e:
        print("Time out!")
        return None
    except Exception:
        print("Not found!")
        return None

#自动点击登录按钮，输入用户名，等待密码输入框出现并输入密码
def login():
    # 点击登录
    login = choose('//*[@id="userLoginInfo"]/span/a[1]')
    login.click()
    username = choose('//*[@id="login_email"]')
    username.send_keys(USERNAME)
    """
    由于密码框控件被设置为不可见
    先自行输入密码并记住密码
    方便刷新
    (也可用cookie实现)
    """
    password = choose('//*[@id="login_pwd_txt"]')
    try:
        password.click()
        password.send_keys("********")
    except Exception:
        print(password)
        print("Password Can't click")

#自动执行购票流程，包括选择票价、点击立即抢购、选择购票人、提交订单等
def buy():
    # 点击价格
    try:
        price = None
        plus = None
        buybtn = None
        submit = None
        booker = None
        select = None
        confirm = None
        driver.get(URL)
        # 选择价格
        while None == price:
            # 这里选的是580票面的，如果选其他票面，修改最后的li[*]即可
            price = choose('//*[@id="priceList"]/div/ul/li[3]')
        price.click()
        # 数量加1 增加购买数量
        while None == plus:
            plus = choose('//*[@id="cartList"]/div[1]/ul/li/span[3]/a[2]')
        plus.click()
        # 立即抢购
        while None == buybtn:
            buybtn = choose('//*[@id="btnBuyNow"]')
        driver.execute_script("arguments[0].scrollIntoView();", buybtn) 
        buybtn.click()
        # 选择购票人
        while None == booker:
            booker = choose('/html/body/div[3]/div[3]/div[2]/div[2]/div/a')
        driver.execute_script("arguments[0].scrollIntoView();", booker) 
        booker.click()
        # 选择、确定
        while None == select:
            select = choose('/html/body/div[3]/div[3]/div[12]/div/div[2]/div/div[2]/div/table/tbody/tr/label/td[1]/input')
        driver.execute_script("arguments[0].scrollIntoView();", select) 
        select.click()
        while None == confirm:
            confirm = choose('/html/body/div[3]/div[3]/div[12]/div/div[2]/div/p/div/a')
        driver.execute_script("arguments[0].scrollIntoView();", confirm) 
        confirm.click()
        # 提交订单
        while None == submit:
            submit = choose('//*[@id="orderConfirmSubmit"]')
        driver.execute_script("arguments[0].scrollIntoView();", submit) 
        submit.click()
    except Exception:
        print("抢票失败，尝试重新抢票")
        buy()

#调用登录和购票函数，用于测试整个流程
def test():
    login()
    time.sleep(30)
    print("开始抢票")
    buy()
    print("抢票成功")


"""
移动端抢票操作
"""

def login_mobile():
    """
    点击购买进入登录界面
    自行输入帐号密码
    """
    # 立即购买
    buybtn = None
    while None == buybtn:
        buybtn = choose('/html/body/div[1]/div[2]/div/div[1]/div[2]/div')
    driver.execute_script("arguments[0].scrollIntoView();", buybtn) 
    buybtn.click()
    # 默认已经选好时间了，再点击立即购买
    buy = None
    while None == buy:
        buy = choose('/html/body/div[1]/div[3]/div[2]/div[1]/div')
    driver.execute_script("arguments[0].scrollIntoView();", buy) 
    buy.click()

def buy_mobile():
    try:
        # 立即购买
        buybtn = None
        while None == buybtn:
            buybtn = choose('/html/body/div[1]/div[2]/div/div[1]/div[2]/div')
        driver.execute_script("arguments[0].scrollIntoView();", buybtn) 
        buybtn.click()
        # 默认已经选好时间了，再点击立即购买
        buy = None
        while None == buy:
            buy = choose('/html/body/div[1]/div[3]/div[2]/div[1]/div')
        driver.execute_script("arguments[0].scrollIntoView();", buy) 
        buy.click()
        # 580票面
        price = None
        while None == price:
            price = choose('//html/body/div[1]/div/div[2]/ul/li[3]')
        driver.execute_script("arguments[0].scrollIntoView();", price) 
        price.click()
        # 数量+1
        count = None
        while None == count:
            count = choose('/html/body/div[1]/div/div[3]/ul/li/div/div[3]')
        driver.execute_script("arguments[0].scrollIntoView();", count) 
        count.click()
        # 选好了
        select = None
        while None == select:
            select = choose('/html/body/div[1]/div/div[4]/div[3]')
        driver.execute_script("arguments[0].scrollIntoView();", select) 
        select.click()
        # 购票人
        booker = None
        while None == booker:
            booker = choose('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/ul/li/div')
        driver.execute_script("arguments[0].scrollIntoView();", booker) 
        booker.click()
        # 去付款
        pay = None
        while None == pay:
            pay = choose('/html/body/div[1]/div[2]/div[2]/div[2]/div')
        driver.execute_script("arguments[0].scrollIntoView();", pay) 
        pay.click()
    except Exception:
        print("抢票失败，尝试重新抢票")
        buy_mobile()

def test_mobile():
    login_mobile()
    time.sleep(30)
    print("开始抢票")
    buy_mobile()
    print("抢票成功")

def main():
    # 默认PC网页，手机网页对应修改即可
    login()
    # 30秒等待用户输入密码后再开始刷
    time.sleep(30)
    while 1:
        if MIN == time.localtime().tm_min:
            print("开始抢票")
            buy()
            print("抢票成功")

if __name__ == '__main__':
    test()
    #test_mobile()
    #main()
