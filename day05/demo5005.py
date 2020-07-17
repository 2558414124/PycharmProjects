from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
# ECShop商城前台首页
driver.get("http://localhost/upload/index.php")
# 点击一个元素
a = driver.find_elements(By.TAG_NAME,"img")
a[1].click()
sleep(3)
driver.quit()
