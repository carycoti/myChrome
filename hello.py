#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def main():
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(60)
    # browser = webdriver.Chrome()
    # browser.maximize_window()

    # url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    # browser.get(url)
    try:
        browser.get('https://baidu.com')
    except TimeoutException:
        print('Time Out')
    try:
        browser.find_element_by_id('kw').send_keys('hello world')
        browser.find_element_by_id('su').click()
        print(browser.title)
        time.sleep(6)
    except NoSuchElementException:
        print('No Element')

    browser.execute_script("window.open('https://www.zhihu.com/')", "")
    time.sleep(5)
    browser.get('https://www.zhihu.com/')
    print(browser.title)
    browser.quit()


if __name__ == "__main__":
    main()
