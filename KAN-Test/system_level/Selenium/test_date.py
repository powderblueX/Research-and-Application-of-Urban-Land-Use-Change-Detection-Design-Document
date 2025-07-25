import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://43.142.162.35:5173/#/login"

class DateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def login(self):
        driver = self.driver
        driver.get(BASE_URL)
        time.sleep(5)
        user_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Email/UserName"]')))
        user_input.send_keys("xyy")
        pwd_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Password"]')))
        pwd_input.send_keys("123456")
        login_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "登录")]')))
        login_btn.click()
        self.wait.until(EC.url_contains("/grid"))
        time.sleep(5)

    def test_date(self):
        driver = self.driver
        self.login()
        driver.get("http://43.142.162.35:5173/#/grid")
        select = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'el-select')))
        select.click()
        option = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "夜晚地表平均温度")]')))
        option.click()
        time.sleep(10)

if __name__ == "__main__":
    unittest.main() 