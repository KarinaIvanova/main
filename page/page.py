#coding: utf-8

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from page.locators import LoginFormLocators
from page.locators import SearchResultLocators


class CheckLoginToVk(object):

    def check_login_vk(Config, name_of_test, driver, url):
        driver.get(url)
        login_vk = driver.find_element_by_xpath(LoginFormLocators.login_xpath)
        login_vk.clear()
        login_vk.send_keys(Config.login_vk)
        password_vk = driver.find_element_by_xpath(LoginFormLocators.password_xpath)
        password_vk.clear()
        password_vk.send_keys(Config.password_vk)
        button_vk = driver.find_element_by_xpath(LoginFormLocators.button_log_in_xpath)
        button_vk.click()
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, SearchResultLocators.my_page_xpath))
            )
            #print('yraaaaaa!!!' + str(name_of_test) + ' done!!!')
        finally:
            driver.maximize_window()
            screen_name = 'screen_' + str(name_of_test) + '.png'
            driver.save_screenshot(screen_name)