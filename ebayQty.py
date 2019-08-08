#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class EbayQty():
    def __init__(self):
        # chrome_options = Options()
        # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # self.driver = webdriver.Chrome(options=chrome_options)

        location = r'E:\scoop\apps\firefox\current\firefox.exe'
        self.driver = webdriver.Firefox(firefox_binary=location)

        self.driver.implicitly_wait(30)
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def ebay_qty(self):
        self.driver.get("https://secure.pushauction.com/Listing/Listing.aspx?parentID=103&page=10&btn=hrefListOnline/")
        self.driver.maximize_window()
        # self.driver.find_element(By.ID, "txtUserID").click()
        # self.driver.find_element(By.ID, "txtUserID").click()
        # element = self.driver.find_element(By.ID, "txtUserID")
        # actions = ActionChains(self.driver)
        # actions.double_click(element).perform()
        # self.driver.find_element(By.ID, "btnLogin").click()
        # element = self.driver.find_element(By.LINK_TEXT, "4797")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # self.driver.find_element(By.ID, "Nav103").click()
        # self.driver.find_element(By.LINK_TEXT, "在线").click()
        # self.driver.find_element(By.ID, "txtKeyword").click()
        WebDriverWait(self.driver, 120, 1).until(
            EC.presence_of_element_located((By.ID, 'txtKeyword'))
        )
        self.driver.find_element(By.ID, "txtKeyword").send_keys('251959314797')
        time.sleep(5)
        # self.driver.find_element(By.ID, "btnSearch").send_keys(Keys.ENTER)
        # element = self.driver.find_element(By.ID, "btnSearch")
        self.driver.execute_script('document.getElementById("btnSearch").click();')
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # actions.click(element).perform()
        # element = self.driver.find_element(By.ID, "btnSearch")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # element = self.driver.find_element(By.CSS_SELECTOR, "body")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        time.sleep(3)
        self.driver.find_element(By.ID, "rpeBayListLog_lblActionMenu_0").click()
        self.driver.find_element(By.LINK_TEXT, "在线编辑").click()
        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME,'dialog_frame'))
        self.driver.find_element(By.ID, "chkSelQTY").click()
        self.driver.find_element(By.ID, "btnGoEdit").click()
        self.driver.find_element(By.CSS_SELECTOR, "#panQTY .control-label").click()
        self.driver.find_element(By.ID, "txtAvailableQTY").click()
        self.driver.find_element(By.ID, "txtAvailableQTY").send_keys("5")
        self.driver.find_element(By.ID, "btnGoToConfirm").click()
        self.driver.find_element(By.ID, "btnUpdate").click()


if __name__ == '__main__':
    browser = EbayQty()
    browser.ebay_qty()
