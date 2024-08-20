from selenium.webdriver.common.by import By
import time

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    ADD_TO_CART_BUTTON = (By.XPATH, ".//a")

    def add_to_cart(self):
        container = self.driver.find_element(By.ID, 'tbodyid')
        button = container.find_element(By.XPATH, ".//a")
        button.click()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()