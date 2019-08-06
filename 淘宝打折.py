#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models import MyDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class TaobaoDiscount():
    def __init__(self):
        self.driver = MyDriver.chrome_dev()
        self.url = "http://yx1.shendusou.com/bootstrapweb/tpls/main/index.jsp?firstshow=ntd"
        self.account_list = ['happycoti', '时尚健康作坊']

    def teardown_method(self):
        self.driver.quit()

    def login(self, account):
        self.driver.get('https://login.taobao.com')
        try:
            self.driver.find_element(By.CLASS_NAME, 'static').click()
        except Exception:
            pass
        WebDriverWait(self.driver, 60, 0.5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'J_UserName'))
        )
        self.driver.find_element(By.CLASS_NAME, 'J_UserName').send_keys(Keys.CONTROL, 'a')
        self.driver.find_element(By.CLASS_NAME, 'J_UserName').send_keys(account)
        self.driver.find_element(By.ID, 'J_SubmitStatic').click()
        # btn_slide = self.driver.find_element(By.CLASS_NAME, 'btn_slide')
        # if btn_slide:
        #     time.sleep(5)
        #     action = ActionChains(self.driver)
        #     action.click_and_hold(btn_slide).move_by_offset(298, 11).perform()
        #     time.sleep(10)
        #     self.driver.find_element(By.ID, 'J_SubmitStatic').click()

    def run(self):
        for account in self.account_list:
            try:
                self.login(account)
                WebDriverWait(self.driver, 120, 1).until_not(
                    EC.presence_of_element_located((By.CLASS_NAME, 'J_Submit'))
                )
                self.driver.get('http://container.open.taobao.com/container?appkey=12326907&a=auth')
                self.driver.find_element(By.ID, 'sub').click()
                self.driver.get(self.url)
                WebDriverWait(self.driver, 600, 1).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'data_container'))
                )
                showtid = self.driver.find_elements(By.CLASS_NAME, 'showtid')
                drop_down_lists = self.driver.find_elements(By.CLASS_NAME, 'data_container')
                m = 0
                time.sleep(5)
                for item in drop_down_lists:
                    time.sleep(3)
                    showtid[m].click()
                    item.find_element(By.CLASS_NAME, 'upbasesetmodal').click()
                    time.sleep(2)
                    self.driver.find_element(By.LINK_TEXT, "7天").click()
                    time.sleep(1)
                    self.driver.find_element(By.CSS_SELECTOR, ".pull-right:nth-child(2)").click()
                    m += 1
                self.driver.get('http://yx1.shendusou.com/bootstrapweb/tpls/main/indexstopped.jsp')
                # 已结束的活动，如果有要重新编写，未完成
                if self.driver.find_element(By.TAG_NAME, 'h2'):
                    pass
            except (NoSuchElementException, TimeoutException) as e:
                print(e)
            finally:
                self.teardown_method()


if __name__ == '__main__':
    browser = TaobaoDiscount()
    browser.run()
