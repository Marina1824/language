import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    yield browser
    print("\nquit browser..")
    browser.quit()