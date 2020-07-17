from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
# 打开ECShop前台首页
driver.get("http://localhost/upload/index.php")
# 打开登录页面
dl = driver.find_element(By.XPATH,"//font/a[1]")
dl.click()
# 输入用户名和密码
yhm = driver.find_element(By.NAME,"username")
yhm.send_keys("lisi")
mm = driver.find_element(By.NAME,"password")
mm.send_keys("123456")
# 点击登录submit
ljdl = driver.find_element(By.NAME,"submit")
ljdl.click()
# 点击用户中心//font/a[1]
yhzx = driver.find_element(By.XPATH,"//font/a[1]")
yhzx.click()
# 点击左侧用户信息//div[@class='userMenu']/a[2]/img
yhxx = driver.find_element(By.XPATH,"//div[@class='userMenu']/a[2]/img")
yhxx.click()
# 获得右侧电子邮件地址文本框里的当前内容,存储在变量e1中email
dzyx = driver.find_element(By.NAME,"email")
e1 = dzyx.get_attribute("value")
print(e1)
# 点击留言板//div/a[10]
lyb = driver.find_element(By.XPATH,"//div/a[10]")
lyb.click()
# 获得留言板页面里的电子邮件地址文本框的当前内容user_email,存储在e2中
dzyj = driver.find_element(By.NAME,"user_email")
e2 = dzyj.get_attribute("value")
print(e2)
# 使用if语句判断e1是否等于e2
# 如果相等,在日志打印"邮箱正确",否则打印"邮箱错误"
if e1 == e2:
    print("邮箱正确")
else:
    print("邮箱错误")
# 等待1秒
sleep(1)
# 判断匿名留言复选框当前没有被选中,就点击它
nmly = driver.find_element(By.ID,"anonymous")
zt1=nmly.is_selected()
print(zt1)
if not zt1:#zt1 == false
    nmly.click()
# 判断留言类型中的第4个单选按钮,如果当前没有被选中,就点击选中它
sh = driver.find_element_by_xpath("//td[2]/input[4]")
zt2 = sh.is_selected()
print(zt2)
if not zt2:
    sh.click()
# 点击退出//font/a[2]
tc = driver.find_element(By.XPATH,"//font/a[2]")
tc.click()
# 等待3秒
sleep(3)
# 关闭浏览器
sleep(3)
driver.quit()