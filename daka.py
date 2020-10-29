import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

class user(object):
    def __init__(self,uid,pwd):
        self.uid=uid
        self.pwd=pwd

    def sign_in(self):
        option=webdriver.ChromeOptions()
        option.add_argument('headless') # 设置option
        browser = webdriver.Chrome(chrome_options=option)
        #设置运行时不显示浏览器窗口
        browser.get("http://login.cuit.edu.cn/Login/xLogin/Login.asp")

        try:
            browser.find_element_by_name('txtId').send_keys(self.uid)
            browser.find_element_by_name('txtMM').send_keys(self.pwd)
            browser.find_element_by_id('IbtnEnter').click()
            time.sleep(0.5)
            t = time.strftime('%m%d',time.localtime())
            browser.find_element_by_link_text(t+'疫情防控——师生健康状态采集').click()
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
            browser.find_element_by_name("B2").click()
            print(t+'打卡成功！')

        except Exception as e:
            print("there is an exception:" + str(e))
            print('打卡失败')
        finally:
            browser.quit()
def main():
    u1 = user("2018122017","GJL053132a")
    u1.sign_in()
    time.sleep(1)
    u2 = user("2017121162","GJJ040200a")
    u2.sign_in()
    print("大功告成！！！")

if __name__ == "__main__":
    main()
