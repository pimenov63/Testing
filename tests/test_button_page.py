import allure

from pages.simple_button import SimpleButtonPage


@allure.feature('Simple button')
@allure.story('existence')
def test_button1_exist(browser):
    with allure.step('Open Simple button page'):
        simple_page = SimpleButtonPage(browser)
        simple_page.open()
    with allure.step('Check the button'):

        assert simple_page.button_is_displayed()

    # browser.get('https://www.qa-practice.com/elements/button/simple')
    # browser.find_element(By.ID, 'submit-id-submit').click()
    # assert 'Submitted' == browser.find_element(By.ID, 'result-text').text


@allure.feature('Simple button')
@allure.story('clickability')
def test_button1_clicked(browser):
    with allure.step('Open Simple button page'):
        simple_page = SimpleButtonPage(browser)
        simple_page.open()
    with allure.step('Click the button'):
        simple_page.click_button()
    with allure.step('Chec the result'):
        assert 'Submitted' == simple_page.result_text
