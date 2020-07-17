from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
# 打开前台首页
driver.get("http://localhost/upload/index.php")
# 定位关键字文本框,赋值给变量
gjz = driver.find_element(By.ID,"keyword")
gjz.send_keys("a")
gjz.send_keys("b")
gjz.send_keys("c")
# 点击搜索
ss = driver.find_element(By.NAME,"imageField")
ss.click()
gjz = driver.find_element(By.ID,"keyword")
# 输入关键字d
gjz.send_keys("d")
# xpath定位左上角ECShop商标
ecshop = driver.find_element_by_xpath("html/body/div[1]/div[1]/a/img")
ecshop.click()

sleep(3)
driver.quit()