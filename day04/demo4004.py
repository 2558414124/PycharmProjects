from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
# 启动火狐浏览器
driver = webdriver.Firefox()
# 打开ECShop前台登录页面
driver.get("http://localhost/upload/user.php")
# 输入用户名lisi
yhm=driver.find_element(By.NAME,'username')
yhm.send_keys('lisi')
# 定位密码框
mm=driver.find_element(By.NAME,'password')
mm.send_keys('123456')
# 点击立即登陆
ljdl=driver.find_element(By.NAME,'submit')
ljdl.click()
# 等待5秒
sleep(5)
# 定位退出按钮,点击退出
tc=driver.find_element_by_link_text('退出')
tc.click()
sleep(4)
# 关闭浏览器
driver.quit()
