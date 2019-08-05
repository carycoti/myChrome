#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class MyDriver(object):
    def __init__(self):
        pass

    def chrome_dev(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        browser = webdriver.Chrome(options=chrome_options)
        browser.implicitly_wait(30)
        return browser


if __name__ == "__main__":
    pass




