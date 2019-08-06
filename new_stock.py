#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models import MyDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import win32api


class NewStock():
    def __init__(self):
        self.driver = MyDriver.chrome_dev()
        self.url = "https://www.jisilu.cn/data/new_stock/#apply"

    def teardown_method(self):
        self.driver.quit()

    def run(self):
        try:
            self.driver.get(self.url)
            stock_table = self.driver.find_element(By.ID, 'flex_apply')
            stocks = stock_table.find_element(
                By.TAG_NAME, 'tbody').find_elements(
                By.TAG_NAME, 'tr')
            today_stocks = [i.find_element(By.CSS_SELECTOR, 'td[data-name="stock_cd"]').text for i in stocks if
                            '今日' in i.find_element(By.CSS_SELECTOR, 'td[data-name="apply_dt"]').text]
            result = 'GOOD LUCK!'
            if len(today_stocks) > 0:
                for stock in today_stocks:
                    result = f'{stock}\n{result}'
                result = result.strip(', ')
                win32api.MessageBox(0, result, "今日可申购新股")
        except (NoSuchElementException, TimeoutException) as e:
            print(e)
        finally:
            self.teardown_method()


if __name__ == '__main__':
    browser = NewStock()
    browser.run()
