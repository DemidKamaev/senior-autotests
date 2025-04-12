from project_avto_ui_5_2.base_page import BasePage


class CheckoutPage(BasePage):
    BUTTON_CHECKOUT_SELECTOR = '[id="checkout"]'
    FIRST_NAME_SELECTOR = '[id="first-name"]'
    LAST_NAME_SELECTOR = 'input[name="lastName"]'
    POSTAL_CODE_SELECTOR = '#postal-code'
    BUTTON_CONTINUE_SELECTOR = '#continue'
    BUTTON_FINISH_SELECTOR = '#finish'
    URL_OVERVIEW = 'https://www.saucedemo.com/checkout-step-two.html'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-step-one.html'

    def start_check_in_form(self):
        self.wait_for_selector_and_click(self.BUTTON_CHECKOUT_SELECTOR)
        self.assert_element_is_visible(self.FIRST_NAME_SELECTOR)

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.wait_for_selector_and_type(self.FIRST_NAME_SELECTOR, first_name, 150)
        self.wait_for_selector_and_type(self.LAST_NAME_SELECTOR, last_name, 100)
        self.wait_for_selector_and_type(self.POSTAL_CODE_SELECTOR, postal_code, 50)
        self.assert_input_value(self.POSTAL_CODE_SELECTOR, postal_code)
        self.assert_element_is_visible(self.BUTTON_CONTINUE_SELECTOR)
        self.wait_for_selector_and_click(self.BUTTON_CONTINUE_SELECTOR)
        self.assert_url_is_correct(self.URL_OVERVIEW)
        self.assert_text_present_on_page('Checkout: Overview')
