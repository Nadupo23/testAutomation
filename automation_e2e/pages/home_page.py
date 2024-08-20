from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    product = (By.ID, 'tbodyid')
    navbar = (By.ID, 'navbarExample')

    def select_product(self, index):
        products = self.driver.find_element(*self.product)
        product_element = products.find_elements(By.XPATH, "./*")[index]
        link_product = product_element.find_element(By.XPATH, ".//a")
        link_product.click()

    def back_to_home(self):
        home = self.driver.find_element(*self.navbar)
        link_home = home.find_elements(By.XPATH, "./*")[0].find_element(By.XPATH, ".//a")
        link_home.click()