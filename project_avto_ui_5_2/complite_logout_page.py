from project_avto_ui_5_2.base_page import BasePage


class CheckoutCompletePage(BasePage):
    CHECKOUT_COMPLETE_SELECTOR = 'span[class="title"]'
    TEXT_THANK_YOU = 'h2.complete-header'
    TEXT_COMPLETE_MESSAGE = 'div.complete-text'
    IMG_SUCCESS = 'img.pony_express'
    BUTTON_BACK_HOME = 'button#back-to-products'
    BURGER_SELECTOR = '#react-burger-menu-btn'
    ALL_ITEMS_SELECTOR = 'a#inventory_sidebar_link'
    BUTTON_ABOUT_SELECTOR = 'a#about_sidebar_link'
    LOGOUT_SELECTOR = '#logout_sidebar_link'
    RESET_APP_STATE_SELECTOR = '#reset_sidebar_link'
    LOGOUT_URL = 'https://www.saucedemo.com/'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-complete.html'


    def assert_all_elements_page(self):
        self.assert_text_in_element(self.CHECKOUT_COMPLETE_SELECTOR, "Checkout: Complete!")
        self.assert_element_is_visible(self.IMG_SUCCESS)
        self.assert_text_in_element(self.TEXT_THANK_YOU, "Thank you for your order!")
        self.assert_element_is_visible(self.CHECKOUT_COMPLETE_SELECTOR)
        self.assert_element_is_visible(self.BUTTON_BACK_HOME)
        self.assert_element_is_visible(self.BURGER_SELECTOR)

    def click_burger_menu(self):
        self.wait_for_selector_and_click(self.BURGER_SELECTOR)
        self.assert_element_is_visible(self.ALL_ITEMS_SELECTOR)
        self.assert_element_is_visible(self.BUTTON_ABOUT_SELECTOR)
        self.assert_element_is_visible(self.LOGOUT_SELECTOR)
        self.assert_element_is_visible(self.RESET_APP_STATE_SELECTOR)


    def logout(self):
        self.wait_for_selector_and_click(self.LOGOUT_SELECTOR)
        self.assert_url_is_correct(self.LOGOUT_URL)