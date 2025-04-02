from selenium.webdriver.common.by import By
from pageObjects.checkout import CheckoutConfirmation
from utils.browserUtils import BrowserUtils

class ShopPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.XPATH, "//a[text()='Shop']")
        self.product_cards = (By.XPATH, "//div/app-card-list/app-card")
        self.go_to_checkout = (By.CSS_SELECTOR, ".btn-primary")



    def add_product_to_cart(self,mobile):
        # can also done by using CSS_SELECTOR "a[href*='shop']" (regular expression *=)
        self.driver.find_element(*self.shop_link).click()

        # Store web-elements of all product in a list ---
        app_cards = self.driver.find_elements(*self.product_cards)
        print(len(app_cards))
        for each_card in app_cards:
            current_text = each_card.find_element(By.CSS_SELECTOR, "div h4 a").text
            if current_text == mobile:
                # Add product to the cart
                each_card.find_element(By.CSS_SELECTOR, ".btn-info").click()
                break


    def go_to_cart(self):
        # checkout
        self.driver.find_element(*self.go_to_checkout).click()
        checkout_obj = CheckoutConfirmation(self.driver)
        return checkout_obj