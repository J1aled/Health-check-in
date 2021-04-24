import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import smtplib
from email.mime.text import MIMEText
from email.header import Header

class user(object):
    def __init__(self,uid,pwd):
        self.uid=uid
        self.pwd=pwd

    def sign_in(self):
        option = webdriver.ChromeOptions()
        option.add_argument('headless') # 设置option
        browser = webdriver.Chrome(chrome_options=option)
        # 设置运行时不显示浏览器窗口
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
            print(t+'打卡成功！')
            return True

        except Exception as e:
            print("there is an exception:" + str(e))
            print('打卡失败')
            return False
        finally:
            browser.quit()

def send_email(mail_text):
    from_addr = "GHJKL777@126.com"
    password = 'BCLLVAOISZZYGEWK'

    to_addr = "1971346995@qq.com"

    msg = MIMEText(mail_text)
    msg['Subject'] = "每日健康打卡通知"
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)

    try:
        server = smtplib.SMTP_SSL("smtp.126.com",465)
        server.login(from_addr,password)
        server.sendmail(from_addr,to_addr,msg.as_string())
        server.quit()
        print("邮件发送成功")
    except Exception as e:
        print("Error: 无法发送邮件" + str(e))


def main():
    u1 = user("2018122017","GJL053132a")
    flag1 = (u1.sign_in())
    time.sleep(3)
    u2 = user("2017121162","GJJ040200a")
    flag2 = (u2.sign_in())

    t = time.strftime('%m月%d日',time.localtime())
    if flag1 == False:
        u1.sign_in()
    if flag2 == False:
        u2.sign_in()

    if flag1 == True and flag2 == True:
        mail_text = t+" 健康打卡打卡成功！"
        send_email(mail_text)
    else:
        mail_text = t+"健康打卡打卡失败！"
        send_email(mail_text)


if __name__ == "__main__":
    main()
