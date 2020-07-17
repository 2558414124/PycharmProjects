from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
# 导入select类
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
# 打开ECShop前台首页
driver.get("http://localhost/upload/index.php")
# 选择下拉列表里的选项"充值卡"选项category
f = driver.find_element(By.ID,"category")
s1 = Select(f)
s1.select_by_visible_text("充值卡")


# 关闭浏览器
sleep(3)
driver.quit()