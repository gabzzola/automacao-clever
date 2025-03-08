import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.warehouse.registrations.main import Registrations
from utils.format_price import format_price
from utils.selenium_utils import wait_element_clickable
from utils.element_utils import click_element_add, click_element_save_and_quit

class Ingredients(Registrations):
    def click_element_ingredients(self):
        element = wait_element_clickable(self.driver, By.CSS_SELECTOR, "a[href='#/estoque/insumos']")
        element.click()

    def register(self): 
        self.click_element_warehouse()
        self.click_element_registrations()
        self.click_element_ingredients()
        self.register_ingredients()

    def register_ingredients(self):
        for row in self.dataframe.itertuples():
            ingredient = row.insumo
            price = row.valor_insumo
            
            if not pd.isna(ingredient): 
                formatted_ingredient = ingredient.upper()
                
                time.sleep(2)

                click_element_add(self.driver)
                element_description = wait_element_clickable(self.driver, By.ID, "descricao")
                element_description.send_keys(formatted_ingredient + Keys.TAB)

                if not pd.isna(price):
                    price_formatted = format_price(price)
                    element_price = self.driver.switch_to.active_element
                    element_price.send_keys(price_formatted)
                
                click_element_save_and_quit(self.driver)