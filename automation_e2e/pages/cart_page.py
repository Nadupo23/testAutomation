from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    CART_BUTTON = (By.ID, "cartur")
    CHECKOUT_BUTTON = (By.CLASS_NAME, "btn.btn-success")

    def ir_a_carrito(self):
        button_cart = self.driver.find_element(*self.CART_BUTTON)
        button_cart.click()

    def proceder_a_pagar(self):
        button_pay = self.driver.find_element(*self.CHECKOUT_BUTTON)
        button_pay.click()
