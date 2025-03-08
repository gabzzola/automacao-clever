from selenium.webdriver.common.by import By
from pages.warehouse.registrations.main import Registrations
from utils.selenium_utils import wait_element_clickable

class DeliveryGroup(Registrations):
    def click_element_delivery_group(self):
        element = wait_element_clickable(self.driver, By.CSS_SELECTOR, "a[href='#/estoque/grupos']")
        element.click()

    def register(self):
        self.click_element_warehouse()
        self.click_element_registrations()
        self.click_element_delivery_group()
        self.register_groups(self.dataframe, "grupo_delivery")
