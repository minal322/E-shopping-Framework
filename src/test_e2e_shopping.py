from selenium import webdriver
import sys
import os
import json
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pageObjects.login import LoginPage
from pathlib import Path

#read userdata
test_data_file_path = Path(__file__).parent.parent / "data" / "data_config.json"
print(test_data_file_path)
# test_data_file_path = "../data/data_config.json"
# #test_data_file_path = "data/data_config.json"

with open(test_data_file_path) as file_data:
    test_data = json.load(file_data)
    test_list = test_data["data"]
    print(test_list)

#create custom markers "ecommerce"
@pytest.mark.ecommerce
@pytest.mark.parametrize("test_data_list",test_list)
def test_shop(browserInstance,test_data_list):
    driver = browserInstance
    #Login
    login_obj = LoginPage(driver)
    print(login_obj.getTitle())
    shop_obj = login_obj.login(test_data_list["userEmail"],test_data_list["userPassword"])

    #Shop
    print(shop_obj.getTitle())
    shop_obj.add_product_to_cart(test_data_list["product_name"])
    checkout_obj = shop_obj.go_to_cart()

    #checkout , Address and validation
    print(shop_obj.getTitle())
    checkout_obj.checkout()
    checkout_obj.enter_delivery_address(test_data_list["country"])
    checkout_obj.validate_order()


