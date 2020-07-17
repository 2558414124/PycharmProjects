from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
# 打开前台首页
driver.get("http://localhost/upload/index.php")
# 点击登录--顶级层
d1=driver.find_element(By.ID,'ECS_MEMBERZONE').\
    find_element(By.TAG_NAME,'img')
d1.click()
# 点击注册
zc = driver.find_element(By.ID,"ECS_MEMBERZONE").find_elements\
    (By.TAG_NAME,"img")[1]
zc.click()
# 点击左上角的商标图片
sbtp = driver.find_element(By.NAME,"top").find_element(By.TAG_NAME,"img")
sbtp.click()
sleep(3)
driver.quit()
