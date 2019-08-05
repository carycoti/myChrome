#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import datetime
import random
from selenium.webdriver.common.keys import Keys
from models import MyDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

my_today = datetime.date.today()
next_month = datetime.date(my_today.year, my_today.month + 2, 1)  # 当前日期的下下个月1号
end_day = next_month + datetime.timedelta(days=-1)  # 当前日期下个月最后一天
begin_day = datetime.date(end_day.year, end_day.month, 1)  # end_day当月第一天，也就是当前日期下个月第一天


def main():
    url = 'https://gsp.aliexpress.com/apps/promotion/single/index'
    driver = MyDriver()
    browser = driver.chrome_dev()
    browser.get(url)

    WebDriverWait(browser, 600, 0.5).until(
        EC.presence_of_element_located((By.NAME, 'createPromotion')))
    browser.find_element_by_name('createPromotion').click()
    promotion_time = browser.find_element_by_class_name(
        'dada-date-with-timezone-wrapper')
    promotion_time.find_element_by_class_name(
        'next-range-picker-trigger').click()
    start_date = browser.find_element_by_class_name(
        'next-range-picker-panel-input-start-date')
    start_date.find_element_by_tag_name('input').send_keys(str(begin_day))
    end_date = browser.find_element_by_class_name(
        'next-range-picker-panel-input-end-date')
    end_date.find_element_by_tag_name('input').send_keys(str(end_day))
    end_time = browser.find_element_by_class_name(
        'next-range-picker-panel-input-end-time')
    end_time_input = end_time.find_element_by_tag_name('input')
    end_time_input.click()
    end_time_input.send_keys(Keys.CONTROL, 'a')
    end_time.find_element_by_tag_name('input').send_keys('23:59:59')
    promotion_name = browser.find_element_by_name('promotionName')
    promotion_name.send_keys(f'{begin_day.month:02}{begin_day.day:02}{end_day.month:02}{end_day.day:02}{int(random.random()*10000)}')
    browser.find_element_by_class_name('next-btn-primary').click()

    WebDriverWait(browser, 120, 1).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'dialog-t-button'))
    )
    browser.find_element_by_class_name('dialog-t-button').click()
    WebDriverWait(browser, 120, 1).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'next-input-group-auto-width'))
    )
    discount = browser.find_element_by_class_name('next-input-group-auto-width')
    discount.find_element_by_tag_name('input').send_keys('38')
    browser.find_element_by_class_name('next-dialog-btn').click()

    try:
        WebDriverWait(browser, 60, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'next-pagination-ellipsis'))
        )
        try:
            browser.find_element_by_class_name('dada-progress-dialog-error-info')
            browser.refresh()
            browser.find_element_by_class_name('dialog-t-button').click()
            discount = browser.find_element_by_class_name('next-input-group-auto-width')
            discount.find_element_by_tag_name('input').send_keys('38')
            browser.find_element_by_class_name('next-dialog-btn').click()
            try:
                WebDriverWait(browser, 30, 2).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'dada-progress-dialog-error-info'))
                )
                error_info = browser.find_element(By.CLASS_NAME, 'dada-progress-dialog-error-info').text
                error_info_link = browser.find_element(By.CLASS_NAME, 'dada-progress-dialog')
                error_info_link = error_info_link.find_element_by_tag_name('a').get_attribute('href')
                print(error_info, error_info_link)
            except (TimeoutException, NoSuchElementException):
                save = browser.find_element(By.CLASS_NAME, 'parent-submitButton')
                save.find_element(By.CLASS_NAME, 'next-btn-primary').click()
                print("打折成功")
        except (TimeoutException, NoSuchElementException):
            save = browser.find_element(By.CLASS_NAME, 'parent-submitButton')
            save.find_element(By.CLASS_NAME, 'next-btn-primary').click()
            print("打折成功")
    except (TimeoutException, NoSuchElementException):
        browser.refresh()
        browser.find_element_by_class_name('dialog-t-button').click()
        discount = browser.find_element_by_class_name('next-input-group-auto-width')
        discount.find_element_by_tag_name('input').send_keys('38')
        browser.find_element_by_class_name('next-dialog-btn').click()
        try:
            WebDriverWait(browser, 60, 2).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'next-pagination-ellipsis'))
            )
            try:
                browser.find_element_by_class_name('dada-progress-dialog-error-info')
                browser.refresh()
                browser.find_element_by_class_name('dialog-t-button').click()
                discount = browser.find_element_by_class_name('next-input-group-auto-width')
                discount.find_element_by_tag_name('input').send_keys('38')
                browser.find_element_by_class_name('next-dialog-btn').click()
                try:
                    WebDriverWait(browser, 60, 2).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'dada-progress-dialog-error-info'))
                    )
                    error_info = browser.find_element(By.CLASS_NAME, 'dada-progress-dialog-error-info').text
                    error_info_link = browser.find_element(By.CLASS_NAME, 'dada-progress-dialog')
                    error_info_link = error_info_link.find_element_by_tag_name('a').get_attribute('href')
                    print(error_info, error_info_link)
                except (TimeoutException, NoSuchElementException):
                    save = browser.find_element(By.CLASS_NAME, 'parent-submitButton')
                    save.find_element(By.CLASS_NAME, 'next-btn-primary').click()
            except NoSuchElementException:
                save = browser.find_element(By.CLASS_NAME, 'parent-submitButton')
                save.find_element(By.CLASS_NAME, 'next-btn-primary').click()
        except (TimeoutException, NoSuchElementException):
            error_info = browser.find_element(By.CLASS_NAME, 'dada-progress-dialog-error-info').text
            error_info_link = browser.find_element(By.CLASS_NAME, 'dada-progress-dialog')
            error_info_link = error_info_link.find_element_by_tag_name('a').get_attribute('href')
            print(error_info, error_info_link)
    finally:
        browser.quit()


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end-start)
