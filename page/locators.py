#coding: utf-8


class LoginFormLocators(object):

    login_xpath = '// *[@ id = "index_email"]'
    password_xpath = '//*[@id="index_pass"]'
    button_log_in_xpath = '//*[@id="index_login_button"]'


class SearchResultLocators(object):

    my_page_xpath = '//*[@id="l_pr"]/a/span/span[3]'