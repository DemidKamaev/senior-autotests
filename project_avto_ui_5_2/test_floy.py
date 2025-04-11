from project_avto_ui_5_2.conftest import browser
from project_avto_ui_5_2.login_page import LoginPage
from project_avto_ui_5_2.inventory_page import InventoryPage
from project_avto_ui_5_2.checkout_page import CheckoutPage
from project_avto_ui_5_2.logout_page import LogoutPage


def test_place_an_order(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    logout_page = LogoutPage(page)

    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_first_item_to_shop()
    checkout_page.start_check_in_form()
    checkout_page.fill_checkout_form("Demid", "Kam", "124")
    logout_page.start_burger()
    logout_page.logout()
