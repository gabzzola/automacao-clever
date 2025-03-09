import time
from pages.login import System
from user_action import get_user_action
from execute_action import execute_action
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

        execute_action(user_action, driver)

    except Exception as e:
        print(f"Ocorreu um erro {e}")

    finally:
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    main()
