import time
from selenium import webdriver
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestPurchaseFlow:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.demoblaze.com/")
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()

    def test_login(self):
        home_page = HomePage(self.driver)
        product_page = ProductPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        time.sleep(2)

        # Product one
        home_page.select_product(0)
        time.sleep(2)
        product_page.add_to_cart()
        home_page.back_to_home()
        time.sleep(2)

        # Product two
        home_page.select_product(1)
        time.sleep(2)
        product_page.add_to_cart()
        home_page.back_to_home()
        time.sleep(2)

        # View cart
        cart_page.ir_a_carrito()
        time.sleep(2)
        cart_page.proceder_a_pagar()
        time.sleep(2)

        # Confirm purchase
        checkout_page.fill_out_form("Nathalia", "Colombia", "Cúcuta", "123456", "November", "2")
        checkout_page.confirm_purchase()
        time.sleep(2)
        checkout_page.confirm_alert()
        time.sleep(2)
