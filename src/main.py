import time
import pandas as pd
from pages.login import System
from pages.warehouse.products.product import Product
from utils.selenium_utils import init_driver

def main():
    url = input("Digite a URL do sistema: ")
    user = input("Digite o nome de usuário para acessar o sistema: ")
    password = input("Digite a senha correspondente ao seu usuário: ")

    driver = init_driver()
    system = System(driver)

    try:
        driver.get(url)
        system.login(user, password)

        almoxarifado_produtos = pd.read_csv("almoxarifado_produtos.csv")
        product = Product(driver, almoxarifado_produtos)
        product.register_all_products()

        time.sleep(5)

    except Exception as e:
        print(f"Ocorreu um erro {e}")

if __name__ == "__main__":
    main()
