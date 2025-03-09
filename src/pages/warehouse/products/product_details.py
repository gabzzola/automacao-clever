import pandas as pd
from selenium.webdriver.common.by import By
from pages.warehouse.products.main import Product
from utils.selenium_utils import wait_element_clickable
from utils.format_price import format_price

class ProductDetails(Product):
    def register(self, row):
        self.code(row)
        self.barcode(row)
        self.description(row)
        self.observations(row)
        self.price(row)
        self.delivery_group(row)

    def code(self, row):
        element = wait_element_clickable(self.driver, By.ID, "codigo")

        if not pd.isna(row.codigo) and isinstance(row.codigo, int):
            element.click()
            element.send_keys(row.codigo)

    def barcode(self, row):
        if not pd.isna(row.codigo_barras) and isinstance(row.codigo_barras, int):
            element = self.driver.find_element(By.ID, "codigo_barras")
            element.click()
            element.send_keys(row.codigo_barras)

    def description(self, row):
        description = row.descricao_produto.upper()

        element = self.driver.find_element(By.ID, "descricao")
        element.click()
        element.send_keys(description)

    def observations(self, row):
        if not pd.isna(row.observacoes):
            element = self.driver.find_element(By.ID, "observacoes")
            element.click()
            element.send_keys(row.observacoes)

    def price(self, row):
        if not pd.isna(row.valor_venda):
            price = format_price(row.valor_venda)

            element = self.driver.find_element(By.ID, "valor")
            element.click()
            element.send_keys(price)

    def delivery_group(self, row):
        self.fill_select(row.grupo_delivery, By.CSS_SELECTOR, "#s2id_grupo_produto_id a.select2-choice.select2-default")
