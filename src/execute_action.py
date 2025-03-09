import pandas as pd
from pages.warehouse.products.main import Product
from pages.warehouse.registrations.main import Registrations

def execute_action(user_action, driver):
    actions = {
        "Cadastro de produtos sem dados para comanda": lambda: register_products_without_order_data(driver),
        "Cadastro de produtos com dados para comanda": lambda: register_products_with_order_data(driver),
        "Cadastro de produtos com dados para comanda, mas Grupo Delivery, Grupo de Itens e Insumos já estão cadastrados": lambda: register_products_without_order_data(driver),
    }
    
    action = actions.get(user_action)
    action()

def register_products_without_order_data(driver):
    try:
        almoxarifado_produtos = pd.read_csv("almoxarifado_produtos.csv")
        product = Product(driver, almoxarifado_produtos)
        product.register_all_products()

    except FileNotFoundError:
        print("Erro: O arquivo 'almoxarifado_produtos.csv' não foi encontrado.")

    except Exception as e:
        print(f"Erro ao cadastrar produtos: {e}")

def register_products_with_order_data(driver):
    try:
        try:
            almoxarifado_cadastros = pd.read_csv("almoxarifado_cadastros.csv")  
        except FileNotFoundError:
            print("Erro: O arquivo 'almoxarifado_cadastros.csv' não foi encontrado.")
            return

        try:
            almoxarifado_produtos = pd.read_csv("almoxarifado_produtos.csv")
        except FileNotFoundError:
            print("Erro: O arquivo 'almoxarifado_produtos.csv' não foi encontrado.")
            return
        
        registrations = Registrations(driver, almoxarifado_cadastros)
        product = Product(driver, almoxarifado_produtos)

        registrations.register()  
        product.register_all_products()    

    except Exception as e:
        print(f"Erro ao cadastrar produtos: {e}")
