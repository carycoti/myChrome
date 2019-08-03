# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#
#
# def main():
#     chrome_options = Options()
#     chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#     browser = webdriver.Chrome(options=chrome_options)
#     browser.implicitly_wait(60)
#     browser.get('https://baidu.com')
#     print(browser.title)
#     browser.find_element_by_id('kw').send_keys('hello world')
#     browser.find_element_by_id('su').click()
#     time.sleep(6)
#     print(browser.title)
#     # browser = webdriver.Chrome()
#     # browser.maximize_window()
#
#     # url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
#     # browser.get(url)
#     # try:
#     #     browser.get('https://baidu.com')
#     # except TimeoutException:
#     #     print('Time Out')
#     # try:
#     #     browser.find_element_by_id('kw').send_keys('hello world')
#     #     browser.find_element_by_id('su').click()
#     #     print(browser.title)
#     #     time.sleep(6)
#     # except NoSuchElementException:
#     #     print('No Element')
#
#     time.sleep(5)
#     # 获取当前窗口句柄（窗口A）
#     handle = browser.current_window_handle
#     # 打开一个新的窗口
#     browser.execute_script("window.open('https://www.zhihu.com/')", "")
#     # 获取当前所有窗口句柄（窗口A、B）
#     handles = browser.window_handles
#     browser.switch_to.window(handles[1])
#     print(browser.title)
#     # 对窗口进行遍历
#     # for newhandle in handles:
#     #     # 筛选新打开的窗口B
#     #     if newhandle != handle:
#     #         # 切换到新打开的窗口B
#     #         browser.switch_to.window(newhandle)
#     #         # 在新打开的窗口B中操作
#     #         print(browser.title)
#     #         # 关闭当前窗口B
#     #         # browser.close()
#     # 切换回窗口A
#     browser.switch_to.window(handles[0])
#     print(browser.title)
#     browser.quit()
#
#
# if __name__ == "__main__":
#     main()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
#
# chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# browser = webdriver.Chrome(options=chrome_options)
# browser.implicitly_wait(20)
# browser.get('https://baidu.com')
# print(browser.title)
# # 新建窗口B
# browser.execute_script('window.open("https://www.zhihu.com/")', '')
# # 获取当前所有窗口句柄（窗口A、B）
# handles = browser.window_handles
# # 直接输入编号进入B窗口
# browser.switch_to.window(handles[1])
# print(browser.title)
# # 输入A窗口编号进行切换
# browser.switch_to.window(handles[0])
# browser.find_element_by_id('kw').send_keys('hello world')
# browser.find_element_by_id('su').click()
# time.sleep(2)
# print(browser.title)
#
# browser.quit()


# import time
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open("https://www.taobao.com")')
# print(browser.window_handles)
# browser.switch_to.window(browser.window_handles[1])
# time.sleep(1)
# browser.switch_to.window(browser.window_handles[0])
# browser.get('https://python.org')

import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()
time.sleep(1)
browser.forward()
browser.close()
