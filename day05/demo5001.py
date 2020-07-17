from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("http://localhost/upload/index.php")
# 查看购物车
ckgwc = driver.find_element(By.LINK_TEXT,"查看购物车")
ckgwc.click()
sleep(1)
# 点击留言板
lyb = driver.find_element(By.LINK_TEXT,"留言板")
lyb.click()
# 留言内容hello
# 语法格式1:
# lynr=driver.find_element_by_tag_name("textarea")
# 语法格式2:
lynr=driver.find_element(By.TAG_NAME,'textarea')
lynr.send_keys("hello")
sleep(5)
# 点击您的购物车中有0键商品,总计金额0元,使用包含"总计
# 金额"作为定位条件
# 语法格式一:
# zjje = driver.find_element_by_partial_link_text("总计金额")
# 语法格式二:
zjje = driver.find_element(By.PARTIAL_LINK_TEXT,"总计金额")
zjje.click()
# 点击包含"原装电池"的超级链接
yzdc = driver.find_element(By.PARTIAL_LINK_TEXT,"原装电池")
yzdc.click()
sleep(3)
driver.quit()
