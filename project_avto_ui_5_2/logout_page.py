from project_avto_ui_5_2.base_page import BasePage

class LogoutPage(BasePage):
    BURGER_SELECTOR = '#react-burger-menu-btn'
    LOGOUT_SELECTOR = '#logout_sidebar_link'

    def start_burger(self):
        self.assert_element_is_visible(self.BURGER_SELECTOR)
        self.wait_for_selector_and_click(self.BURGER_SELECTOR)

    def logout(self):
        self.assert_element_is_visible(self.LOGOUT_SELECTOR)
        self.wait_for_selector_and_click(self.LOGOUT_SELECTOR)