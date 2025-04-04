import os
from pageObjects.tables_webpage import TablesSorting

def test_table_sort(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    tables_obj = TablesSorting(driver)
    tables_obj.sort()
    tables_obj.fetch()
    tables_obj.validate()

