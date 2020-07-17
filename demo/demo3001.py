# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Demo3001(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_demo3001(self):
        driver = self.driver
        driver.get(self.base_url + "/upload/index.php")
        driver.find_element_by_css_selector("#ECS_MEMBERZONE > a > img").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("lisi")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("submit").click()
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"退出"))
        self.assertEqual("lisi", driver.find_element_by_css_selector("font.f4_b").text)
        driver.find_element_by_link_text(u"用户中心").click()
        driver.find_element_by_link_text(u"用户信息").click()
        e = driver.find_element_by_name("email").get_attribute("value")
        driver.find_element_by_link_text(u"留言板").click()
        self.assertEqual(e, driver.find_element_by_name("user_email").get_attribute("value"))
        driver.find_element_by_link_text(u"退出").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
