from selenium.webdriver.common.by import By
from utils.selenium_utils import wait_element_clickable

def click_element_add(driver):
    element = wait_element_clickable(driver, By.XPATH, "//button[@tooltip='Adicionar']")
    driver.execute_script("arguments[0].click();", element)

def click_element_save_and_quit(driver):
    element = wait_element_clickable(driver, By.XPATH, "//button[text()='Salvar e fechar']")
    driver.execute_script("arguments[0].click();", element)
