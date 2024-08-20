from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    NAME = (By.ID, "name")
    COUNTRY = (By.ID, "country")
    CITY = (By.ID, "city")
    CARD = (By.ID, "card")
    MONTH = (By.ID, "month")
    YEAR = (By.ID, "year")
    PURCHASE_BUTTON = (By.XPATH, "//button[@onclick='purchaseOrder()']")
    CONFIRM_BUTTON = (By.CLASS_NAME, "confirm.btn.btn-lg.btn-primary")

    def fill_out_form(self, nombre, pais, ciudad, tarjeta, mes, ano):
        self.driver.find_element(*self.NAME).send_keys(nombre)
        self.driver.find_element(*self.COUNTRY).send_keys(pais)
        self.driver.find_element(*self.CITY).send_keys(ciudad)
        self.driver.find_element(*self.CARD).send_keys(tarjeta)
        self.driver.find_element(*self.MONTH).send_keys(mes)
        self.driver.find_element(*self.YEAR).send_keys(ano)

    def confirm_purchase(self):
        button_buy = self.driver.find_element(*self.PURCHASE_BUTTON)
        button_buy.click()

    def confirm_alert(self):
        button_buy = self.driver.find_element(*self.CONFIRM_BUTTON)
        button_buy.click()
