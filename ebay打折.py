#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import datetime
from models import MyDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

USER_NAME_LIST = [
    'caryelectronics',
    'caryelectronic',
    'carytrade',
]
FIRST_DAY = datetime.datetime.strptime('2019-08-05','%Y-%m-%d')


class EbayDiscount():
    def __init__(self):
        self.driver = MyDriver.chrome_dev()
        self.url = "https://www.ebay.com/sh/mkt/promotionmanager/offertypes?promoType=SALE_EVENT"
        today = datetime.datetime.today()
        three_days = today + datetime.timedelta(days=2)
        self.end_day = str(three_days.day)
        days = (today - FIRST_DAY).days
        nid = days % 3
        self.username = USER_NAME_LIST[nid]

    def teardown_method(self):
        self.driver.quit()

    # 利用浏览器记住密码，从而不用输入密码。如果没记住请先登录一次并让chrome记住密码
    def login(self):
        useid = self.driver.find_element(By.ID, "userid")
        useid.send_keys(Keys.CONTROL, 'a')
        useid.send_keys(self.username)
        self.driver.find_element(By.ID, "sgnBt").click()

    def run(self):
        try:
            self.driver.get(self.url)
            if 'signin.' in self.driver.current_url:
                self.login()
            else:
                user = self.driver.find_element(By.CLASS_NAME, 'sh-member-badge').text.split('\n')[0]
                if self.username != user:
                    self.driver.get('https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&lgout=1')
                    self.driver.get(self.url)
                    self.login()
            while 'Error Page' in self.driver.title:
                self.driver.get(self.url)
                time.sleep(2)
            WebDriverWait(self.driver, 600, 1).until(
                EC.presence_of_element_located((By.ID, 'X_PCT_OFF-discountPercent-0-listbox'))
            )
            self.driver.find_element(By.ID, "X_PCT_OFF-discountPercent-0-listbox").click()
            dropdown = self.driver.find_element(By.ID, "X_PCT_OFF-discountPercent-0-listbox")
            dropdown.find_element(By.XPATH, "//option[. = '38']").click()
            self.driver.find_element(By.ID, "X_PCT_OFF-discountPercent-0-listbox").click()
            self.driver.find_element(By.ID, "freeShipping").click()
            self.driver.find_element(By.ID, "w0-mdmTypes-0").click()
            time.sleep(3)
            self.driver.find_element(By.ID, "w9-w2").click()
            time.sleep(3)
            self.driver.find_element(By.CSS_SELECTOR, ".arrow:nth-child(2)").click()
            self.driver.find_element(By.ID, "rdb-all").click()
            time.sleep(6)
            self.driver.find_element(By.ID, "w0-nav-w1").click()
            time.sleep(3)
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
            Select(self.driver.find_element(By.ID, "end-time-listbox")).select_by_value('1050')
            self.driver.execute_script("window.scrollTo(0,300)")
            self.driver.find_element(By.ID, "offerDesc").send_keys("Save up to 38.0%")
            self.driver.find_element(By.ID, "w0-offerreview-14").click()
            print('Ebay打折成功')
        except (NoSuchElementException, TimeoutException) as e:
            print(e)
        finally:
            self.teardown_method()


if __name__ == '__main__':
    browser = EbayDiscount()
    browser.run()
