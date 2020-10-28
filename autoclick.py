import os
# 方便延时加载
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

# 模拟浏览器打开网站
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
#window电脑本地
# browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver")


def saveFile(message):
    # 保存email内容
    with open("email.txt", 'a+', encoding="utf-8") as email:
        email.write(message+'\n')


def epidemic_auto_checkin():
    browser.get('http://yiqing.ctgu.edu.cn/wx/index/login.do?currSchool=ctgu&CURRENT_YEAR=2019&showWjdc=false&studentShowWjdc=false')
    # 将窗口最大化
    browser.maximize_window()
    # 格式是PEP8自动转的
    # 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
    browser.find_element_by_xpath(
        '//*[@id="username1"]').send_keys(os.environ['ActonMartin_USER'])
    browser.find_element_by_xpath(
        '//*[@id="password1"]').send_keys(os.environ['ActonMartin_PASSWORD'])
    # 在输入用户名和密码之后,点击登陆按钮
    browser.find_element_by_xpath("/html/body/main/section[2]/form/div[3]/input").click()
    time.sleep(10)
    try:
        if("今日已上报" in browser.find_element_by_xpath("/html/body/main/section/header/div[1]/span").text):
            saveFile("明日再来!")
        else:
            browser.find_element_by_xpath("/html/body/main/section/header/div[2]/button").click()
            time.sleep(5)
            sreach_window=browser.current_window_handle
            # 这一句需要更改xpath，进行签到
            browser.find_element_by_xpath("/html/body/main/section/header/div[2]/button").click()
            # js = 'document.getElementById("checkin-div").children[0].click();'
            # browser.execute_script(js)
            print("今日打卡打卡成功")
        time.sleep(3)
        saveFile("签到成功！")
    except NoSuchElementException as e:
        print ("NoSuchElementException!")
        saveFile("签到代码存在异常"+str(e))

def vpn():
    urls = ['https://dogcloud.co/','https://doggetech.com/']
    browser.get('https://doggetech.com/')
    # 将窗口最大化
    browser.maximize_window()
    # 格式是PEP8自动转的
    # 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
    browser.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul[2]/li/a').click()
    browser.find_element_by_xpath(
        '//*[@id="username1"]').send_keys(os.environ['ActonMartin_USER'])
    browser.find_element_by_xpath(
        '//*[@id="password1"]').send_keys(os.environ['ActonMartin_PASSWORD'])
    # 在输入用户名和密码之后,点击登陆按钮
    browser.find_element_by_xpath("/html/body/main/section[2]/form/div[3]/input").click()
    time.sleep(10)
    try:
        if("今日已上报" in browser.find_element_by_xpath("/html/body/main/section/header/div[1]/span").text):
            saveFile("明日再来!")
        else:
            browser.find_element_by_xpath("/html/body/main/section/header/div[2]/button").click()
            time.sleep(5)
            sreach_window=browser.current_window_handle
            # 这一句需要更改xpath，进行签到
            browser.find_element_by_xpath("/html/body/main/section/header/div[2]/button").click()
            # js = 'document.getElementById("checkin-div").children[0].click();'
            # browser.execute_script(js)
            print("今日打卡打卡成功")
        time.sleep(3)
        saveFile("签到成功！")
    except NoSuchElementException as e:
        print ("NoSuchElementException!")
        saveFile("签到代码存在异常"+str(e))

if __name__ == '__main__':
    epidemic_auto_checkin()
    # vpn()
    # 脚本运行成功,退出浏览器
    browser.quit()
