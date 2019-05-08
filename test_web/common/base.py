import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_browser(browser="chrome"):
    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "ie":
        driver = webdriver.Ie()
    else:
        # driver = None
        print("请输入正确的浏览器,例如'chrome','Firefox','ie'")
    return driver


class Base:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()  # 窗口最大化

    def find_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator, timeout=10):
        elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    def click(self, locator, timeout=10):
        element = self.find_element(locator=locator, timeout=timeout)
        element.click()

    def send_keys(self, locator, text, timeout=10):
        element = self.find_element(locator=locator, timeout=timeout)
        element.clear()
        element.send_keys(text)

    def is_text_in_element(self, locator, text, timeout=10):
        try:
            result = WebDriverWait(self.driver, timeout=timeout).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    def is_value_in_element(self, locator, value, timeout=10):
        try:
            result = WebDriverWait(self.driver, timeout=timeout).until(
                EC.text_to_be_present_in_element_value(locator, value))
            return result
        except:
            return False

    def close_browser(self):
        self.driver.quit()



