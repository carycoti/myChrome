#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from models import MyDriver
from selenium.webdriver.common.by import By

driver = MyDriver.chrome_dev()

print(driver.title)
if 'Error Page' in driver.title:
    print('yes')