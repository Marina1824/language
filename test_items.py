from selenium.webdriver.common.by import By
import time

def test_basket(browser):
    time.sleep(5)
    buttons=browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(buttons) == 1, "Кнопка не найдена или их больше 1-й"
