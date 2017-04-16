#coding: utf-8


#Chrome config
class ChromeConfig(object):
    chromedriver_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'


#PageConfig is class for right login and password
class PageConfig(object):

    '''Enter here your login and password to https://vk.com/'''
    login_vk = 'your_email@mail.ru'
    password_vk = 'your_password'


#PageConfigWrong is class for wrong login and password
class PageConfigWrong(object):

    #login_vk and password_vk are wrong login and password to https://vk.com/ here
    login_vk = 'fekla_fortochkina@mail.ru'
    password_vk= '123123123feklafeklafekla'