import time
import pandas as pd
from pages.login import System
from pages.warehouse.products.main import Product
from pages.warehouse.registrations.main import Registrations
from user_action import get_user_action
from utils.selenium_utils import init_driver

def main():
    url = input("Digite a URL do sistema: ")
    user = input("Digite o nome de usuário para acessar o sistema: ")
    password = input("Digite a senha correspondente ao seu usuário: ")

    user_action = get_user_action()

    driver = init_driver()
    system = System(driver)

    try:
        driver.get(url)
        system.login(user, password)

        if (user_action == "Cadastro de produtos sem dados para comanda"):
            almoxarifado_produtos = pd.read_csv("almoxarifado_produtos.csv")
            product = Product(driver, almoxarifado_produtos)
            product.register_all_products()
        elif (user_action == "Cadastro de Grupo Delivery, Grupo de Itens e Insumos"):
            almoxarifado_cadastros = pd.read_csv("almoxarifado_cadastros.csv")
            registrations = Registrations(driver, almoxarifado_cadastros)
            registrations.register()        
        
        time.sleep(5)

    except Exception as e:
        print(f"Ocorreu um erro {e}")

if __name__ == "__main__":
    main()
