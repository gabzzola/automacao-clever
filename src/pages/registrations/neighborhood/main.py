import pandas as pd
from selenium.webdriver.common.by import By
from pages.registrations.main import Registrations
from utils.format_price import format_price
from utils.selenium_utils import wait_element_clickable
from utils.element_utils import click_element_add, click_element_save_and_quit

class Neighborhood(Registrations):
    def __init__(self, driver, dataframe):
        super().__init__(driver)
        self.dataframe = dataframe

    def click_element_neighborhood(self):
        element = wait_element_clickable(self.driver, By.CSS_SELECTOR, "a[href='#/cliente/bairro']")
        element.click()
    
    def register(self):
        self.click_element_registrations()
        self.click_element_neighborhood()
        self.register_neighborhood()   
    
    def register_neighborhood(self):
        for row in self.dataframe.itertuples():
            neighborhood = row.descricao_bairro
            price = row.valor_motoboy
            city = row.cidade

            if pd.isna(neighborhood):
                return
            
            click_element_add(self.driver)
            self.fill_description(neighborhood)
            self.mark_show_delivery()

            if not pd.isna(price):
                self.fill_price(price)

            if not pd.isna(city):
                self.fill_city(city)
            
            click_element_save_and_quit(self.driver)

    def fill_description(self, neighborhood):
        neighborhood = neighborhood.upper()
        element = wait_element_clickable(self.driver, By.ID, "descricao")
        element.click()
        element.send_keys(neighborhood)

    def mark_show_delivery(self):        
        element = self.driver.find_element(By.CSS_SELECTOR, "label[class='onoffswitch-label']")
        element.click()

    def fill_price(self, price):
        price = format_price(price)
        element = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Valor MotoBoy']")
        element.send_keys(price)
    
    def fill_city(self, city):                
        city_state = (city.upper()) + " - RS"

        element = wait_element_clickable(self.driver, By.CSS_SELECTOR, "#s2id_cidade_id a.select2-choice.select2-default")
        element.click()  

        search = wait_element_clickable(self.driver, By.CSS_SELECTOR, "input.select2-input.select2-focused")
        search.send_keys(city)
        
        try:                        
            option = wait_element_clickable(self.driver, By.XPATH, f"//div[contains(text(), '{city_state}')]")
            option.click()

        except Exception as e:
            print(f"Erro ao clicar na opção: {e}") 
