#coding: utf-8

'''
Authorization test on https://vk.com/ site with correct and incorrect login and password
(positive and negative tests) with Google Chrome browser.
Usage:
page object is located in page package.

All locators are in page/locators.py.
Write your login and password to https://vk.com/ in page/element.py in class PageConfig

Write path to chromedriver in in page/element.py in class ChromeConfig

'''


from unittest import TestCase, main
from selenium import webdriver
from page.page import LogInToVk
from page.element import PageConfig
from page.element import PageConfigWrong
from page.element import ChromeConfig
from page.locators import SearchResultLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestLoginToVk(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeConfig.chromedriver_path)
        self.base_url = 'https://vk.com/'

    def test_with_right_login(self):
        'Checks log in with correct login and password. Expects \'Моя странца\' '
        LogInToVk.log_in_to_vk(PageConfig, self.driver, self.base_url)
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, SearchResultLocators.my_page_xpath))
            )
            #print('\nyraaaaaa!!! test_with_right_login is done!!!')
        finally:
            self.driver.maximize_window()
            screen_name = 'screen_test_with_right_login.png'
            self.driver.save_screenshot(screen_name)

    def test_with_wrong_login(self):
        'Checks log in with wrong login and password. Expects \'Unable to log in.\' '
        LogInToVk.log_in_to_vk(PageConfigWrong, self.driver, self.base_url)
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, SearchResultLocators.unable_to_log_in))
            )
            #print('\nyraaaaaa!!! test_with_wrong_login is done!!!')
        finally:
            self.driver.maximize_window()
            screen_name = 'screen_test_with_wrong_login.png'
            self.driver.save_screenshot(screen_name)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    main()
