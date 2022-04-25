import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru')


@pytest.fixture()
def browser(request):
    user_language = request.config.getoption("language")
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(executable_path='C:/Users/petro/Driver/chromedriver.exe', options=options)
    browser.implicitly_wait(10)
    yield browser
    time.sleep(30)
    print("\nquit browser..")
    browser.quit()
