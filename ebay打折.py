#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import datetime
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class EbayDiscount():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(20)
        self.vars = {}
        today = datetime.datetime.today()
        three_days = today + datetime.timedelta(days=2)
        self.end_day = str(three_days.day)

    def teardown_method(self):
        self.driver.quit()

    def run(self):
        try:
            self.driver.get("https://www.ebay.com/sh/mkt/promotionmanager/dashboard")
            self.driver.maximize_window()
            self.driver.find_element(By.ID, "promo-menu-button").click()
            self.driver.find_element(By.ID, "dashboard-w1-w4").click()
            self.driver.find_element(By.ID, "X_PCT_OFF-discountPercent-0-listbox").click()
            dropdown = self.driver.find_element(By.ID, "X_PCT_OFF-discountPercent-0-listbox")
            dropdown.find_element(By.XPATH, "//option[. = '38']").click()
            self.driver.find_element(By.ID, "X_PCT_OFF-discountPercent-0-listbox").click()
            self.driver.find_element(By.ID, "freeShipping").click()
            self.driver.find_element(By.ID, "w0-mdmTypes-0").click()
            time.sleep(2)
            self.driver.find_element(By.ID, "w9-w2").click()
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, ".arrow:nth-child(2)").click()
            self.driver.find_element(By.ID, "rdb-all").click()
            # self.driver.execute_script("window.scrollTo(0,300)")
            time.sleep(6)
            self.driver.find_element(By.ID, "w0-nav-w1").click()
            time.sleep(2)
            self.driver.find_element(By.ID, "start-time-listbox").click()
            dropdown = self.driver.find_element(By.ID, "start-time-listbox")
            dropdown.find_element(By.XPATH, "//option[. = 'Start now']").click()
            self.driver.find_element(By.ID, "start-time-listbox").click()
            try:
                self.driver.find_element(By.CSS_SELECTOR, "#w0-offerreview-end-cal > .ui-datepicker-trigger").click()
                self.driver.find_element(By.ID, "prev-label").click()
                self.driver.find_element(By.LINK_TEXT, self.end_day).click()
            except NoSuchElementException:
                self.driver.find_element(By.ID, 'next-label').click()
                self.driver.find_element(By.LINK_TEXT, self.end_day).click()

            self.driver.find_element(By.ID, "end-time-listbox").click()
            dropdown = self.driver.find_element(By.ID, "end-time-listbox")
            dropdown.find_element(By.XPATH, "//option[. = '5:30pm PDT']").click()
            self.driver.execute_script("window.scrollTo(0,300)")
            self.driver.find_element(By.ID, "offerDesc").send_keys("Save up to 38.0%")
            self.driver.find_element(By.ID, "w0-offerreview-14").click()
        except (NoSuchElementException, TimeoutException) as e:
            print(e)
        finally:
            self.teardown_method()


if __name__ == '__main__':
    browser = EbayDiscount()
    browser.run()
