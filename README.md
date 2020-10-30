# python+GitHub_Actions实现自动打卡

#*python*  #**Actions**  #*成都信息工程大学*  #*健康打卡*

##### 打卡模块

需要先安装selenium库

> pip install selenium

导入库函数：

> ```python
> from selenium import webdriver
> from selenium.webdriver.support.select import Select
> from selenium.webdriver.chrome.options import Options
> ```

代码实现：

> ```python
>   def sign_in(self):
>      option=webdriver.ChromeOptions()
>      option.add_argument('headless') # 设置option
>      browser = webdriver.Chrome(chrome_options=option)
>      #设置运行时不显示浏览器窗口
>      browser.get("http://login.cuit.edu.cn/Login/xLogin/Login.asp")
>      try:
>        browser.find_element_by_name('txtId').send_keys(self.uid)
>        browser.find_element_by_name('txtMM').send_keys(self.pwd)
>        browser.find_element_by_id('IbtnEnter').click()
>        time.sleep(0.5)
>        t = time.strftime('%m%d',time.localtime())
>        browser.find_element_by_link_text(t+'疫情防控——师生健康状态采集').click()
>        time.sleep(0.5)
>        s1 = Select(browser.find_element_by_name("sF21650_5"))
>        s1.select_by_value("1")
>        s2 = Select(browser.find_element_by_name("sF21650_6"))
>        s2.select_by_value("1")
>        s3 = Select(browser.find_element_by_name("sF21650_7"))
>        s3.select_by_value("1")
>        s4 = Select(browser.find_element_by_name("sF21650_8"))
>        s4.select_by_value("1")
>        s5 = Select(browser.find_element_by_name("sF21650_9"))
>        s5.select_by_value("1")
>        browser.find_element_by_name("B2").click()
>        print(t+'打卡成功！')
>        return True
>      except Exception as e:
>        print("there is an exception:" + str(e))
>        print('打卡失败')
>        return False
>      finally:
>        browser.quit()
> ```

##### 邮件提醒

打卡成功后发送邮件提醒

需要使用SMTP服务，安装smtplib

> pip search smtplib

选择一个合适的即可

> pip install py-emails

导入库：

> ```python
> import smtplib
> from email.mime.text import MIMEText
> from email.header import Header
> ```

实现：

> ```python
> msg = MIMEText(mail_text)
> msg['Subject'] = "每日健康打卡通知"
> msg['From'] = Header(from_addr)
> msg['To'] = Header(to_addr)
> try:
>    server = smtplib.SMTP_SSL("smtp.126.com",465)
>    server.login(from_addr,password)
>    server.sendmail(from_addr,to_addr,msg.as_string())
>    server.quit()
>    print("邮件发送成功")
> except Exception as e:
>    print("Error: 无法发送邮件" + str(e))
> ```

##### 部署到Actions

> 其实就是对项目代码进行自动化测试，从而保证push代码的正确性。利用action功能，你可以选择github提供的各种测试环境(windows，Linux, MaxOS)运行你的项目。

`GitHub Actions`内有一些概念性的定义，如下所示：

- **workflow**：顾名思义这是工作流程，在`GitHub Actions`中每执行一次就是一个工作流程。
- **job**：工作流程中的一个任务，一个工作流程可以配置多个任务
- **step**：工作任务中的步骤，根据配置的先后顺序执行，一个任务内可以配置多个步骤
- **action**：每个步骤所使用的构建动作，可以使用`GitHub`官方提供的动作实现，也可以自动编写。
