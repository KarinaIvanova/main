'''
Authorization test on https://vk.com/ site with correct and incorrect login and password
(positive and negative tests) with Google Chrome browser.
Usage:
page object is located in page package.

All locators in page/locators.py.
Write your login and password to https://vk.com/ in page/element.py in class PageConfig

Write path to chromedriver in in page/element.py in class ChromeConfig

'''

#coding: utf-8

from unittest import TestCase, main
from selenium import webdriver
from page.page import CheckLoginToVk
from page.element import PageConfig
from page.element import PageConfigWrong
from page.element import ChromeConfig


class TestLoginToVk(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeConfig.chromedriver_path)
        self.base_url = 'https://vk.com/'

    def test_with_right_login(self):
        CheckLoginToVk.check_login_vk(PageConfig, 'test_with_right_login', self.driver, self.base_url)

    def test_with_wrong_login(self):
        CheckLoginToVk.check_login_vk(PageConfigWrong, 'test_with_wrong_login', self.driver, self.base_url)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    main()
