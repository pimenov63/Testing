# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# from config import Config


# @pytest.fixture(scope="session")
# def browser():
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.maximize_window()
#     yield driver
#     driver.quit()
# import os
# # import sys
# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# #
# from config import Config

# # print("Current working directory:", os.getcwd())
# # print("Python path:", sys.path)


# @pytest.fixture(scope="session")
# def browser():
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.maximize_window()
#     driver.get(Config.BASE_URL)
#     yield driver
#     driver.quit()


# @pytest.fixture(scope="session")
# def browser():
#     options = Options()
#     # Здесь можно добавить настройки options, если нужно

#     browser.maximize_window()
#     browser.get(Config.BASE_URL)
#     yield browser
#     browser.quit()
import pytest
from selenium import webdriver


@pytest.fixture()
def browser():

    chrome_browser = webdriver.Chrome()
    chrome_browser.maximize_window()
    chrome_browser.implicitly_wait(10)
    return chrome_browser
