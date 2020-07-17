from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
# 打开ECShop前台首页
driver.get("http://localhost/upload/index.php")
# 输入关键字
gjz = driver.find_element(By.CSS_SELECTOR,"#keyword")
gjz.send_keys("a")
# 点击搜索
ss = driver.find_element(By.CSS_SELECTOR,".go")
ss.click()
sleep(3)
driver.quit()