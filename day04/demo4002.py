from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
# 启动浏览器
driver = webdriver.Firefox()
# 打开ECshop首页
driver.get("http://localhost/upload/index.php")
# 定义关键字文本框,然后输入a
# id定位的语法格式一:
# gjz = driver.find_element_by_id("keyword")
# gjz.send_keys("a")
# id定位的语法格式二: ---推荐使用二!
gjz = driver.find_element(By.ID,"keyword")
gjz.send_keys("a")
# 定位搜索按钮,点击它
# name定位的语法格式一:
# ss = driver.find_element_by_name("imageField")
# name定位的语法格式二:
ss = driver.find_element(By.NAME,"imageField")
ss.click()
# 等待3秒
sleep(3)
# 关闭浏览器
driver.quit()
