from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.selenium_utils import wait_element_clickable

class System:
    def __init__(self, driver):
        self.driver = driver

    def login(self, user, password):
        element_user = wait_element_clickable(self.driver, By.CSS_SELECTOR, "input[placeholder='Usuário']")
        element_user.clear()
        element_user.send_keys(user + Keys.TAB)

        element_password = self.driver.switch_to.active_element
        element_password.send_keys(password, Keys.TAB)

        enter_button = self.driver.switch_to.active_element
        enter_button.send_keys(Keys.ENTER)
