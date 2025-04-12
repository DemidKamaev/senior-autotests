from project_avto_ui_5_2.base_page import BasePage

class CheckOverviewPage(BasePage):
    TITLE_SELECTOR = '.title'
    ITEM_SELECTOR = '.cart_item'
    ORDER_SUMMARY_INFO = '.summary_info'
    BTN_CANCEL_SELECTOR = '#cancel'
    BTN_FINISH_SELECTOR = '#finish'
    CHECK_OVERVIEW_URL = 'https://www.saucedemo.com/checkout-step-two.html'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-step-two.html'

    def assert_checkout_overview_element(self):
        self.assert_text_in_element(self.TITLE_SELECTOR, "Checkout: Overview")
        self.assert_element_is_visible(self.ITEM_SELECTOR)
        self.assert_element_is_visible(self.ORDER_SUMMARY_INFO)
        self.assert_element_is_visible(self.BTN_CANCEL_SELECTOR)
        self.assert_element_is_visible(self.BTN_FINISH_SELECTOR)
        self.assert_text_in_element(self.BTN_FINISH_SELECTOR, "Finish")

    def button_finish_click(self):
        if self._get_full_url() == self.CHECK_OVERVIEW_URL:
            self.wait_for_selector_and_click(self.BTN_FINISH_SELECTOR)

