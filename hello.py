#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def main():
    browser = webdriver.Chrome()
    browser.maximize_window()

    # url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    # browser.get(url)
    try:
        browser.get('https://gsp.aliexpress.com/apps/promotion/single/index')
    except TimeoutException:
        print('Time Out')
    try:
        browser.find_element_by_id('hello')
    except NoSuchElementException:
        print('No Element')
    finally:

        time.sleep(6)
        browser.close()

if __name__ == "__main__":
    main()
