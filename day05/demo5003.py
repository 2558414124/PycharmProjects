from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("http://localhost/upload/index.php")
# 查看购物车
ckgwc = driver.find_element(By.LINK_TEXT,"查看购物车")
ckgwc.click()
sleep(1)
# 点击页面左上角ECShop商标
tp = driver.find_element(By.TAG_NAME,"textarea")
tp.click()
sleep(3)
driver.quit()
