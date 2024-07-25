# from selenium.webdriver.common.by import By

# from pages.base_page import BasePage

# button_selector = (By.LINK_TEXT, 'Click')
# result_selector = (By.ID, 'result-text')


# class LikeAButton(BasePage):
#     def __init__(self, browser):
#         super().__init__(browser)

#     def open(self):
#         self.browser.get(
#             'https://www.qa-practice.com/elements/button/like_a_button')

#     def button(self):
#         return self.find(button_selector)

#     def button_is_displayed(self):
#         return self.button_is_displayed()

#     def button_click(self):
#         return self.button().click()

#     def result(self):
#         return self.find(result_selector)

#     @property
#     def result_text(self):
#         return self.result().text
import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

button_selector = (By.LINK_TEXT, 'Click')
result_selector = (By.ID, 'result-text')


class LikeAButton(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        with allure.step('Open Like a button page'):
            self.browser.get(
                'https://www.qa-practice.com/elements/button/like_a_button')

    def button(self):
        return self.find(button_selector)

    def button_is_displayed(self):
        with allure.step('Check the button is diplayed'):
            return self.button().is_displayed()

    def button_click(self):
        with allure.step('Click the button'):
            self.button().click()

    def result(self):
        return self.find(result_selector)

    @property
    def result_text(self):
        with allure.step('Get result text'):
            return self.result().text
