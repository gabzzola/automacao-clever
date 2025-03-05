import pandas as pd
from selenium.webdriver.common.by import By
from pages.warehouse.warehouse import Warehouse
from utils.selenium_utils import wait_element_clickable
from utils.element_utils import click_element_add, click_element_save_and_quit

class Registrations(Warehouse):
    def __init__(self, driver, dataframe):
        super().__init__(driver)
        self.dataframe = dataframe

    def click_element_registrations(self):
        element = wait_element_clickable(self.driver, By.XPATH, "//span[contains(text(), 'Almoxarifado')]/ancestor::li//span[contains(text(), 'Cadastros')]")
        element.click()

    def register(self):        
        from pages.warehouse.registrations.item_group import ItemGroup
        from pages.warehouse.registrations.ingredients import Ingredients
        from pages.warehouse.registrations.delivery_group import DeliveryGroup
        
        item_group = ItemGroup(self.driver, self.dataframe)
        ingredients = Ingredients(self.driver, self.dataframe)
        delivery_group = DeliveryGroup(self.driver, self.dataframe)

        item_group.register()
        ingredients.register()
        delivery_group.register()

    def register_groups(self, dataframe, item_column):
        registered = set()

        for row in dataframe.itertuples():
            item = getattr(row, item_column)

            if not pd.isna(item) and item not in registered:
                formatted_item = item.upper()
                
                click_element_add(self.driver)
                element = wait_element_clickable(self.driver, By.ID, "descricao")
                element.send_keys(formatted_item)
                click_element_save_and_quit(self.driver)

                registered.add(item)
