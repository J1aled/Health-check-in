import os
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class CUIT(object):
    def __init__(self, uid, pwd):
        self.uid = uid
        self.pwd = pwd

    def sign_in(self):
        chrome_options = chrome_options()
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
        browser.get("http://login.cuit.edu.cn/Login/xLogin/Login.asp")

        try:
            browser.find_element_by_name('txtId').send_keys(self.uid)
            browser.find_element_by_name('txtMM').send_keys(self.pwd)
            browser.find_element_by_id('IbtnEnter').click()
            time.sleep(0.5)

            t = time.strftime('%m%d', time.localtime())
            browser.find_element_by_link_text(t + '疫情防控——师生健康状态采集').click()
            time.sleep(0.5)

            s1 = Select(browser.find_element_by_name("sF21650_5"))
            s1.select_by_value("1")
            s2 = Select(browser.find_element_by_name("sF21650_6"))
            s2.select_by_value("1")
            s3 = Select(browser.find_element_by_name("sF21650_7"))
            s3.select_by_value("1")
            s4 = Select(browser.find_element_by_name("sF21650_8"))
            s4.select_by_value("1")
            s5 = Select(browser.find_element_by_name("sF21650_9"))
            s5.select_by_value("1")
            s6 = Select(browser.find_element_by_name("sF21912_1"))
            s6.send_keys("北街")
            s6 = Select(browser.find_element_by_name("sF21912_2"))
            s6.send_keys("买生活用品")
            s7 = Select(browser.find_element_by_name("sF21912_3"))
            s7.select_by_value("1")
            s8 = Select(browser.find_element_by_name("sF21912_4"))
            s8.select_by_value("06")
            s9 = Select(browser.find_element_by_name("sF21912_5"))
            s9.select_by_value("3")
            s10 = Select(browser.find_element_by_name("sF21912_6"))
            s10.select_by_value("23")
            browser.find_element_by_name("B2").click()
            saveFile(t + '打卡成功！')

        except Exception as e:
            print("there is an exception:" + str(e))
            saveFile("打卡失败：签到代码存在异常" + str(e))
        finally:
            browser.quit()


def saveFile(message):
    # 保存email内容
    with open("email.txt", 'a+', encoding="utf-8") as email:
        email.write(message + '\n')


def main():
    username = os.environ["CUIT_USER"]
    passowrd = os.environ["CUIT_PASSWORD"]
    user = CUIT(username, passowrd)
    user.sign_in()


if __name__ == "__main__":
    main()
