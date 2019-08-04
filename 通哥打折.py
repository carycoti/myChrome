#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import datetime
from selenium.webdriver.common.keys import Keys
from models import MyDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random

my_today = datetime.date.today()
begin_day = my_today + datetime.timedelta(days=-1)
next_month = datetime.date(my_today.year, my_today.month+2, 1)
end_day = next_month + datetime.timedelta(days=-1)

def main():
    url = 'https://gsp.aliexpress.com/apps/promotion/single/index'
    driver = MyDriver(url)
    browser = driver.chrome_dev()

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

    WebDriverWait(browser, 60, 0.5).until(
        EC.presence_of_element_located((By.NAME, 'createPromotion')))
    browser.find_element_by_name('createPromotion').click()
    # time.sleep(random.randrange(6))
    promotion_time = browser.find_element_by_class_name(
        'dada-date-with-timezone-wrapper')
    promotion_time.find_element_by_class_name(
        'next-range-picker-trigger').click()
    # time.sleep(random.randrange(3))
    start_date = browser.find_element_by_class_name(
        'next-range-picker-panel-input-start-date')
    start_date.find_element_by_tag_name('input').send_keys(str(begin_day))
    # time.sleep(1)
    end_date = browser.find_element_by_class_name(
        'next-range-picker-panel-input-end-date')
    end_date.find_element_by_tag_name('input').send_keys(str(end_day))
    # time.sleep(2)
    end_time = browser.find_element_by_class_name(
        'next-range-picker-panel-input-end-time')
    end_time_input = end_time.find_element_by_tag_name('input')
    end_time_input.click()
    # time.sleep(3)
    end_time_input.send_keys(Keys.CONTROL, 'a')
    # time.sleep(1)
    end_time.find_element_by_tag_name('input').send_keys('23:59:59')
    # time.sleep(1)
    promotion_name = browser.find_element_by_name('promotionName')
    promotion_name.send_keys(f'{begin_day.month:02}{begin_day.day:02}{end_day.month:02}{end_day.day:02}')
    # time.sleep(1)
    # browser.find_element_by_class_name('next-btn-primary').click()
    browser.quit()


if __name__ == "__main__":
    # pwd = input('Pls enter the password: ')
    # main(pwd)
    main()
