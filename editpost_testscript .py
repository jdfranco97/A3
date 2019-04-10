import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class addPost(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()

    def test_blog(self):
        driver = self.driver
        user = "admin"
        pwd = "password123"
        driver.maximize_window()
        driver.get("http://rentadev.pythonanywhere.com/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://rentadev.pythonanywhere.com/")
        assert "Logged In"
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[2]/ul/li[2]").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_title")
        elem.send_keys("This is a test post with selenium")
        elem = driver.find_element_by_id("id_text")
        elem.send_keys("This is a test post of text with selenium")
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id='id_java']").click()
        elem = driver.find_element_by_xpath("//*[@id='id_python']").click()
        elem = driver.find_element_by_xpath("//*[@id='id_other']").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/form/button").click()
        time.sleep(2)
        assert "Posted Post"
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/a[1]").click()
        elem = driver.find_element_by_id("id_text")
        elem.send_keys(" This is a post edit, performed by selenium.")
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/form/button").click()
        time.sleep(2)



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

