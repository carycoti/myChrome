#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models import MyDriver
from selenium.common.exceptions import NoSuchElementException

def main():
    driver = MyDriver()
    browser = driver.chrome_dev()
    # ret = browser.find_element_by_class_name('dada-progress-dialog-label')
    # ret2 = ret.find_element_by_class_name('value')
    # print(ret2.text)
    try:
        browser.find_element_by_class_name('dada-progress-dialog-error-info')
    except NoSuchElementException:
        print('Not Found')
    browser.quit()


if __name__ == '__main__':
    main()
