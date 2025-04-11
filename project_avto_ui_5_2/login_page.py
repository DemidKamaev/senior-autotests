from project_avto_ui_5_2.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = ''

    USER_NAME_SELECTOR = '#user-name'
    PASS_WORD_SELECTOR = '#password'
    LOG_BUTTON_SELECTOR = '#login-button'

    def login(self, username, password):
        self.navigate_to()
        self.wait_for_selector_and_fill(self.USER_NAME_SELECTOR, username)
        self.wait_for_selector_and_fill(self.PASS_WORD_SELECTOR, password)
        self.wait_for_selector_and_click(self.LOG_BUTTON_SELECTOR)
        self.assert_text_present_on_page('Products')
