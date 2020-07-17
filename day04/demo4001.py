from selenium import webdriver
from time import sleep
# 启动浏览器
driver = webdriver.Firefox()
# 打开ECshop登录页面
driver.get("http://localhost/upload/user.php")
# ......
# 等待3秒
sleep(3)
# 关闭浏览器
driver.quit()
