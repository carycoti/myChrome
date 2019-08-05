#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models import MyDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def main():
    driver = MyDriver()
    browser = driver.chrome_dev()
    # ret = browser.find_element_by_class_name('dada-progress-dialog-label')
    # ret2 = ret.find_element_by_class_name('value')
    # print(ret2.text)
    error_info = browser.find_element(By.CLASS_NAME, 'dada-progress-dialog-error-info').text
    error_info_link = browser.find_element(By.CLASS_NAME, 'dada-progress-dialog').find_element_by_tag_name('a').get_attribute('href')
    print(error_info, error_info_link)


if __name__ == '__main__':
    main()
