import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.login_admin_page import LoginAdminPage

class Test_01_Admin_Login:
    admin_page_url = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"
    invalid_username = "admin@yorurstore.com"

    def test_title_verification(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        title = self.driver.title
        expected_title = "nopCommerce demo store. Login"
        if title == expected_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.driver.close()
            assert False

    def test_valid_admin_login(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)

        self.login_object = LoginAdminPage(self.driver)
        self.login_object.enter_username(self.username)
        self.login_object.enter_password(self.password)
        self.login_object.login()

        expected_text = "Dashboard"
        actual_text = self.driver.find_element(By.XPATH,"//div[@class='content-header']/h1").text
        if actual_text == expected_text:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.driver.close()
            assert False

    def test_invalid_admin_login(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)

        self.login_object = LoginAdminPage(self.driver)
        self.login_object.enter_username(self.invalid_username)
        self.login_object.enter_password(self.password)
        self.login_object.login()

        actual_text = self.driver.find_element(By.XPATH, "//li").text
        if actual_text == "No customer account found":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.driver.close()
            assert False

