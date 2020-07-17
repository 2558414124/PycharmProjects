from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
# 导入Select类
from selenium.webdriver.support.select import Select
driver=webdriver.Firefox()
driver.get("file:///D:/%E5%B7%A5%E4%BD%9C/%E8%B5%B5%E6%99%93%E"
           "5%80%A9/10-selenim%E8%87%AA%E5%8A%A8%E5%8C%96%E6%"
           "B5%8B%E8%AF%95-%E9%83%91%E5%AD%A6%E6%99%B6(15%E5%A"
           "4%A9)/%E7%AC%94%E8%AE%B0/02-selenium05/02-"
           "seleniumday05(for%20student)/day0502demo/demo01."
           "html")
# 城市
c = driver.find_element(By.ID,"city")
s = Select(c)
# 通过文本来选择选项,参数是option和/option之间的全部文本
s.select_by_visible_text("重庆")
sleep(1)
# 通过索引号来选择选项,参数是从0开始编号的书序
# 例如:选择第一个选项(索引号是0)北京
s.select_by_index(0)
sleep(1)
# 通过option标记元素的value属性值来选择
# 例如:选择value属性值是"天津"的选项
s.select_by_value("天津")
# 民族
m = driver.find_element(By.ID,"nation")
z = Select(m)
# 选择文本是回族的选项
z.select_by_visible_text("回族")
sleep(1)
# 选择索引为第3个的选项
z.select_by_index(3)
sleep(1)
# 选择value属性值是满族的选项
z.select_by_value("满族")
sleep(3)
driver.quit()