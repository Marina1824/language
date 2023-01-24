from selenium.webdriver.common.by import By
import time



def test_basket(browser):
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")

