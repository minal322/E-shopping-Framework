from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.browserUtils import BrowserUtils


class CheckoutConfirmation(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver =driver
        self.checkout_button =(By.CSS_SELECTOR, ".btn-success")
        self.country_input =(By.CSS_SELECTOR, ".filter-input")
        self.country_option =(By.CSS_SELECTOR, "div[class='suggestions'] ul li")
        self.checkbox =(By.CSS_SELECTOR, "div label[for='checkbox2']")
        self.purchase_button = (By.CSS_SELECTOR, ".btn-success")
        self.alert_message = (By.CSS_SELECTOR, ".alert-success")

    def checkout(self):
        # payment
        self.driver.find_element(*self.checkout_button).click()

    def enter_delivery_address(self,countryName):
        ###Explicit Wait
        # dynamic input dropdown
        # send India
        self.driver.find_element(*self.country_input).send_keys(countryName)
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located((self.country_option)))
        self.driver.find_element(*self.country_option).click()
        '''
        OR
        #send ind
        driver.find_element(By.CSS_SELECTOR,".filter-input").send_keys("ind")
        wait = WebDriverWait(driver,5)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
        driver.find_element(By.LINK_TEXT,"India").click()
        '''
        # click checkbox
        self.driver.find_element(*self.checkbox).click()

        # purchase

        self.driver.find_element(*self.purchase_button).click()

    def validate_order(self):
        # fetch message and verify
        message = self.driver.find_element(*self.alert_message).text
        print(message)
        assert "Success" in message
