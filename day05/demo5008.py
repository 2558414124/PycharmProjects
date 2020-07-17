from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
# 打开前台留言板
driver.get("http://localhost/upload/message.php")
# 输入电子邮件地址jack@163.com
email = driver.find_element(By.XPATH,"//tr[2]/td/input[1]")
email.send_keys("jack@163.com")
# 在主体文本框内输入"蓝色"
zt = driver.find_element(By.XPATH,"//tr[4]/td[2]/input")
zt.send_keys("蓝色")
# 点击求购单选按钮
qg = driver.find_element(By.XPATH,"//input[5]")
qg.click()
# 输入留言内容hello
lynr = driver.find_element(By.XPATH,"//textarea")
lynr.send_keys("hello")
sleep(3)
driver.quit()