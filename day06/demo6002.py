from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
# 打开ECShop前台首页
driver.get("http://localhost/upload/message.php")
# 留言内容
lynr = driver.find_element(By.NAME,"msg_content")
lynr.send_keys("Hello")
lynr.send_keys("World")
# 获得内容
nr = lynr.get_attribute("value")
print(nr)
sleep(1)
lynr.clear()
lynr.send_keys("武汉加油!\n中国加油!")
sleep(3)
driver.quit()