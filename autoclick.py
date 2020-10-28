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
        saveFile("疫情签到成功！")
    except NoSuchElementException as e:
        print ("NoSuchElementException!")
        saveFile("签到代码存在异常"+str(e))

def vpn1():
    urls = ['https://dogcloud.co/','https://doggetech.com/']
    browser.get(urls[0])
    # 将窗口最大化
    browser.maximize_window()
    # 格式是PEP8自动转的
    # 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
    # 找到登录按钮跳转到登录窗口
    time.sleep(5)
    browser.find_element_by_xpath('//*[@id="navbarSupportedContent"]').click()
    time.sleep(5)
    sreach_window=browser.current_window_handle
    # browser.find_element_by_xpath(
    #     '//*[@id="email"]').send_keys(os.environ['ActonMartin_USER'])
    # browser.find_element_by_xpath(
    #     '//*[@id="password1"]').send_keys(os.environ['ActonMartin_PASSWORD'])
    browser.find_element_by_xpath(
        '//*[@id="email"]').send_keys(os.environ['VPN1_USER'])
    browser.find_element_by_xpath(
        '//*[@id="password"]').send_keys(os.environ['VPN1_PASSWORD'])
    # 在输入用户名和密码之后,点击登陆按钮
    browser.find_element_by_xpath('//*[@id="app"]/section/div/div/div/div[2]/form/div/div[5]/button').click()
    time.sleep(2)
    # 点击弹窗
    browser.find_element_by_xpath('//*[@id="popup-ann-modal"]/div/div/strong/strong/strong/div/button').click()
    time.sleep(2)
    # 点击签到
    try:
        if("明日再来" in browser.find_element_by_xpath('//*[@id="checkin-div"]').text):
            saveFile('vpn1已经签到')
        time.sleep(5)
    except:
        # 点击签到
        browser.find_element_by_xpath('//*[@id="checkin-div"]').click()
        saveFile('vpn1签到成功')
        time.sleep(5)

def vpn2():
    browser.get('https://baipiaoyun.xyz/auth/login')
    # 将窗口最大化
    browser.maximize_window()
    # 格式是PEP8自动转的
    # 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
    # browser.find_element_by_xpath(
    #     '//*[@id="email"]').send_keys(os.environ['ActonMartin_USER'])
    # browser.find_element_by_xpath(
    #     '//*[@id="password1"]').send_keys(os.environ['ActonMartin_PASSWORD'])
    # time.sleep(2)
    # browser.find_element_by_xpath('//*[@id="header"]').click()
    time.sleep(2)
    browser.find_element_by_xpath(
        '//*[@id="email"]').send_keys(os.environ['VPN2_USER'])
    browser.find_element_by_xpath(
        '//*[@id="passwd"]').send_keys(os.environ['VPN2_PASSWORD'])
    # 在输入用户名和密码之后,点击登陆按钮
    browser.find_element_by_xpath('//*[@id="login"]').click()
    time.sleep(5)
    sreach_window=browser.current_window_handle
    try:
        if("今日已签到" in browser.find_element_by_xpath('//*[@id="checkin"]').text):
            saveFile('vpn2已经签到')
        time.sleep(5)
    except:
        # 点击签到
        browser.find_element_by_xpath('//*[@id="checkin"]').click()
        time.sleep(5)

if __name__ == '__main__':
    epidemic_auto_checkin()
    # vpn1()
    vpn2()
    # 脚本运行成功,退出浏览器
    browser.quit()
