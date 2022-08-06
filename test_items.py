from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestMainPage():
    def test_add_to_basket_button(self, browser):
        browser.get(link)

        button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")

        assert button.is_displayed() is True
