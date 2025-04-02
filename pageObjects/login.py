from selenium.webdriver.common.by import By
from pageObjects.shop import ShopPage
from utils.browserUtils import BrowserUtils

class LoginPage(BrowserUtils):
    def __init__(self,driver):
        #initializing parent class constructor
        super().__init__(driver)
        #declaring locators for reusability
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input =(By.ID, "password")
        self.agree_terms_input = (By.ID, "terms")
        self.signin_button = (By.ID, "signInBtn")


    def login(self,username,password):
        # find_element need two params that's why we are using * , * splits tupel in two parts at runtime
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.agree_terms_input).click()
        self.driver.find_element(*self.signin_button).click()

        #creating shop page object and return
        shop_obj = ShopPage(self.driver)
        return shop_obj




