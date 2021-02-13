from selenium import webdriver
import tensorflow as fw

driver = webdriver.Chrome('C:/Users/JongGeun/Desktop/CODING/chromedriver.exe')

driver.get("https://license.korcham.net/kor/member/login.jsp")

driver.find_element_by_id('uid').send_keys('johnbr1212')
driver.find_element_by_id('upwd').send_keys('password')

driver.find_element_by_xpath('//*[@id="idMemberLogin"]/div[1]/div[1]/input').click()
