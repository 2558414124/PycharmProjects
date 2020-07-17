from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("file:///D:/%E5%B7%A5%E4%BD%9C/%E8%B5%B5%E6%99%93"
           "%E5%80%A9/10-selenim%E8%87%AA%E5%8A%A8%E5%8C%96%E"
           "6%B5%8B%E8%AF%95-%E9%83%91%E5%AD%A6%E6%99%B6(15%"
           "E5%A4%A9)/%E7%AC%94%E8%AE%B0/02-selenium04/02"
           "-seleniumday04%EF%BC%88for%20student%EF%BC%89/"
           "seleniumday0401demo/05-classname.html")
# 输入姓名jack
xm =driver.find_element_by_class_name("username")
xm.send_keys("jack")
# 输入密码123456
mm = driver.find_element(By.CLASS_NAME,"password")
mm.send_keys("123")
sleep(3)
driver.quit()
