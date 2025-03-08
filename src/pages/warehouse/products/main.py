import pandas as pd
from selenium.webdriver.common.by import By
from pages.warehouse.main import Warehouse
from utils.selenium_utils import wait_element_clickable
from utils.element_utils import click_element_add, click_element_save_and_quit

class Product(Warehouse):
    def __init__(self, driver, dataframe):
        super().__init__(driver)
        self.dataframe = dataframe

    def click_element_products(self):
        element = wait_element_clickable(self.driver, By.CSS_SELECTOR, "a[href='#/estoque/produtos']")
        element.click()

    def register_all_products(self):
        self.click_element_warehouse()
        self.click_element_products()

        for row in self.dataframe.itertuples():
            self.register_product(row)

    def register_product(self, row):
        from pages.warehouse.products.product_details import ProductDetails

        click_element_add(self.driver)

        details = ProductDetails(self.driver, self.dataframe)
        details.register(row)

        click_element_save_and_quit(self.driver)

    def fill_select(self, value, selector):
        if not pd.isna(value):
            formatted_value = value.upper()

            element = wait_element_clickable(self.driver, By.CSS_SELECTOR, selector)
            element.click()  

            search = wait_element_clickable(self.driver, By.CSS_SELECTOR, "input.select2-input.select2-focused")
            search.send_keys(formatted_value)
            
            try:
                option = wait_element_clickable(self.driver, By.XPATH, f"//div[text()='{formatted_value}']")
                option.click()

            except Exception as e:
                print(f"Erro ao clicar na opção: {e}") 
