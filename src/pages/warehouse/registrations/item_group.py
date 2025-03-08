from selenium.webdriver.common.by import By
from pages.warehouse.registrations.main import Registrations
from utils.selenium_utils import wait_element_clickable

class ItemGroup(Registrations):
    def click_element_item_group(self):
        element = wait_element_clickable(self.driver, By.CSS_SELECTOR, "a[href='#/estoque/grupo_item']")
        element.click()

    def register(self):
        self.click_element_warehouse()
        self.click_element_registrations()
        self.click_element_item_group()
        self.register_groups(self.dataframe, "grupo_item")
