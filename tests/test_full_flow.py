import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import os

SCREENSHOT_DIR = "reports/screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

@pytest.mark.flaky(reruns=1)
def test_full_purchase_flow(page, config, products_list):
    step = 1

    login = LoginPage(page)
    login.goto(config["base_url"])
    page.screenshot(path=f"{SCREENSHOT_DIR}/step{step}_login.png")
    step += 1
    login.login(
        config["credentials"]["valid"]["username"],
        config["credentials"]["valid"]["password"]
    )


    inventory = InventoryPage(page)
    inventory.assert_on_inventory()
    page.screenshot(path=f"{SCREENSHOT_DIR}/step{step}_inventory.png")
    step += 1

    missing = inventory.validate_products_against_list(products_list)
    assert not missing, f"Missing products: {missing}"

    for product in products_list:
        inventory.add_product_to_cart_by_name(product)
    assert inventory.get_cart_count() == len(products_list)
    page.screenshot(path=f"{SCREENSHOT_DIR}/step{step}_added_to_cart.png")
    step += 1

    cart = CartPage(page)
    cart.open_cart()
    page.screenshot(path=f"{SCREENSHOT_DIR}/step{step}_cart_open.png")
    step += 1

    cart_items = cart.get_cart_item_names()
    for product in products_list:
        assert product in cart_items
        
    cart.proceed_to_checkout()
    page.screenshot(path=f"{SCREENSHOT_DIR}/step{step}_checkout_start.png")
    step += 1

    checkout = CheckoutPage(page)
    checkout.fill_customer_info(
        config["customer_info"]["first"],
        config["customer_info"]["last"],
        config["customer_info"]["postal"]
    )
    page.screenshot(path=f"{SCREENSHOT_DIR}/step{step}_filled_customer_info.png")
    step += 1
    checkout.continue_button.click()
    page.wait_for_load_state("networkidle")

    checkout.finish_checkout()

    confirmation = checkout.get_confirmation_text()
    assert confirmation and "THANK YOU" in confirmation.upper()
    page.screenshot(path=f"{SCREENSHOT_DIR}/step{step}_confirmation.png")
