from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
# 打开留言板页
driver.get("http://localhost/upload/message.php")
# 点击留言类型中的第4个按钮(售后)
a=driver.find_elements(By.NAME,"msg_type")
print(type(a))
a[3].click()
sleep(3)
driver.quit()