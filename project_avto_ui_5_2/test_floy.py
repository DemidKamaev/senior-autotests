from project_avto_ui_5_2.conftest import browser
from project_avto_ui_5_2.login_page import LoginPage
from project_avto_ui_5_2.inventory_page import InventoryPage
from project_avto_ui_5_2.checkout_page import CheckoutPage
from project_avto_ui_5_2.checkout_overview_page import CheckOverviewPage
from project_avto_ui_5_2.complite_logout_page import CheckoutCompletePage


def test_place_an_order(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    checkout_overview_page = CheckOverviewPage(page)
    check_complite_page = CheckoutCompletePage(page)

    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_first_item_to_shop()
    checkout_page.start_check_in_form()
    checkout_page.fill_checkout_form("Demid", "Kam", "124")
    checkout_overview_page.assert_checkout_overview_element()
    checkout_overview_page.button_finish_click()
    check_complite_page.assert_all_elements_page()
    check_complite_page.click_burger_menu()
    check_complite_page.logout()
