#coding: utf-8

from page.locators import LoginFormLocators


class LogInToVk(object):

    def log_in_to_vk(Config, driver, url):
        driver.get(url)
        login_vk = driver.find_element_by_xpath(LoginFormLocators.login_xpath)
        login_vk.clear()
        login_vk.send_keys(Config.login_vk)
        password_vk = driver.find_element_by_xpath(LoginFormLocators.password_xpath)
        password_vk.clear()
        password_vk.send_keys(Config.password_vk)
        button_vk = driver.find_element_by_xpath(LoginFormLocators.button_log_in_xpath)
        button_vk.click()