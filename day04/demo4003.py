from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
# 启动浏览器
driver = webdriver.Firefox()
# 打开ECshop前台首页
driver.get("http://localhost/upload/index.php")
# 定位高级搜索,点击它
# link_text定位的语法格式一:
# gjss = driver.find_element_by_link_text("高级搜索")
# link_text定位的语法格式二:
gjss = driver.find_element(By.LINK_TEXT,'高级搜索')
gjss.click()
sleep(2)
# 定位搜索简介复选框,然后点击它
ssjj = driver.find_element(By.ID,"sc_ds")
ssjj.click()
# 定位价格最小值文本框,输入100
jg = driver.find_element_by_id("min_price")
jg.send_keys("100")
# 定位价格最大值文本框,输入800
jg = driver.find_element(By.ID,"max_price")
jg.send_keys("800")
# 等待3秒
sleep(3)
# 关闭浏览器
driver.quit()
