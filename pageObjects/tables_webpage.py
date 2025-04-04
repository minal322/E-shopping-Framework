from selenium.webdriver.common.by import By


class TablesSorting:
    def __init__(self,driver):
        self.driver = driver
        self.sorted_list = []
        self.browser_list = []
        self.column_click=(By.XPATH, "//span[.='Veg/fruit name']")
        self.vegies_names=(By.XPATH, "//tr/td[1]")

    def sort(self):
        # click on table colum 1st
        self.driver.find_element(*self.column_click).click()

    def fetch(self):
        # collecting tables veggies list after clicking(browser sorted list)
        veggies_list = self.driver.find_elements(*self.vegies_names)

        for each_veg in veggies_list:
            veg_name = each_veg.text
            self.sorted_list.append(veg_name)
            self.browser_list.append(veg_name)

        # sorting sorted list now
        self.sorted_list.sort()

    def validate(self):
        # Validating both list are same
        assert self.sorted_list == self.browser_list

