import re
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.warehouse.products.main import Product
from utils.selenium_utils import wait_element_clickable

class ProductOrderData(Product):
    def register(self, row):
        if (self.check_order_data(row)):
            self.click_element_order_data()
            self.order_data(row)
            self.delivery_terminal(row)
            self.item_group_and_ingredient(row)                     

    def check_order_data(self, row): 
        ingredient = row.insumo
        item_group = row.grupo_item        
        order_terminal = row.terminal_comanda
        delivery_terminal = row.terminal_delivery        

        return (not pd.isna(ingredient) and not pd.isna(item_group)) or not pd.isna(order_terminal) or not pd.isna(delivery_terminal)
    
    def click_element_order_data(self):
        element = wait_element_clickable(self.driver, By.CSS_SELECTOR, "li[active='tabComanda'] a")
        element.click()

    def click_element_add_inside_order_data(self):
        element = wait_element_clickable(self.driver, By.CSS_SELECTOR, ".btn.btn-cl.btn-info.btn-xs.btn-block.ng-scope")
        element.click()

    def order_data(self, row):
        self.fill_select(row.terminal_comanda, By.CSS_SELECTOR, "#s2id_terminal_id a.select2-choice.select2-default")

    def delivery_terminal(self, row):
        self.fill_select(row.terminal_delivery, By.CSS_SELECTOR, "#s2id_delivery_terminal_id a.select2-choice.select2-default")

    def item_group_and_ingredient(self, row):
        item_group = row.grupo_item
        ingredient = row.insumo

        if pd.isna(item_group) or pd.isna(ingredient):
            return
        
        list_item_groups = re.sub(r"\s*,\s*", ",", item_group).split(",")
        list_ingredients = re.sub(r"\s*,\s*", ",", ingredient).split(",")

        for group, ing in zip(list_item_groups, list_ingredients):                        
            self.click_element_add_inside_order_data()
            self.add_and_select_item(group, "[id^='grupo_item']", True)
            self.add_and_select_item(ing, "[id^='s2id_produto_id_insumo'] a.select2-choice.select2-default", False)

    def add_and_select_item(self, value, selector, is_select):        
        value = value.upper()
        if is_select:
            element = self.select_last_element(selector)
            Select(element).select_by_visible_text(value)
        else:
            self.fill_select(value, By.CSS_SELECTOR, "[id^='s2id_produto_id_insumo'] a.select2-choice.select2-default")

    def select_last_element(self, selector):
        elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
        return elements[-1]
