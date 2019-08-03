#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver

import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def main():
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(60)
    # browser.get('https://me.csdn.net/ywah6666')
    # browser = webdriver.Chrome()
    # browser.maximize_window()
    # url = 'https://gsp.aliexpress.com/apps/promotion/single/index'
    # browser.get(url)
    # browser.implicitly_wait(60)

    # browser.switch_to.frame('alibaba-login-box')
    # username = browser.find_element_by_id('fm-login-id')
    # username.clear()
    # username.send_keys('order@caryelectronic.com')
    # pwd = browser.find_element_by_id('fm-login-password')
    # pwd.clear()
    # time.sleep(2)
    # pwd.send_keys(password)
    # time.sleep(1)
    # browser.find_element_by_class_name('password-login').click()
    # time.sleep(8)
    browser.find_element_by_name('createPromotion').click()
    time.sleep(5)
    promotion_time = browser.find_element_by_class_name(
        'dada-date-with-timezone-wrapper')
    promotion_time.find_element_by_class_name(
        'next-range-picker-trigger').click()
    time.sleep(1)
    start_date = browser.find_element_by_class_name(
        'next-range-picker-panel-input-start-date')
    start_date.find_element_by_tag_name('input').send_keys('2019-08-02')
    time.sleep(1)
    end_date = browser.find_element_by_class_name(
        'next-range-picker-panel-input-end-date')
    end_date.find_element_by_tag_name('input').send_keys('2019-08-31')
    time.sleep(2)
    end_time = browser.find_element_by_class_name(
        'next-range-picker-panel-input-end-time')
    end_time_input = end_time.find_element_by_tag_name('input')
    end_time_input.click()
    time.sleep(3)
    end_time_input.send_keys(Keys.CONTROL,'a')
    time.sleep(1)
    end_time.find_element_by_tag_name('input').send_keys('23:59:59')
    time.sleep(1)
    promotion_name = browser.find_element_by_name('promotionName')
    promotion_name.clear()
    time.sleep(1)
    promotion_name.send_keys('88888')
    promotion_name.clear()
    promotion_name.send_keys('888888')
    browser.find_element_by_class_name('next-btn-primary').click()

    time.sleep(12)
    browser.execute_script("window.open('https://www.baidu.com/')", "")
    browser.quit()


if __name__ == "__main__":
    # pwd = input('Pls enter the password: ')
    # main(pwd)
    main()
