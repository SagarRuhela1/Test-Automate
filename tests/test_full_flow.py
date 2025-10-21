# tests/test_full_purchase_flow.py
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.flaky(reruns=1)
def test_full_purchase_flow(page, config, products_list):
    login = LoginPage(page)
    login.goto(config["base_url"])
    login.login(
        config["credentials"]["valid"]["username"],
        config["credentials"]["valid"]["password"]
    )

    inventory = InventoryPage(page)
    inventory.assert_on_inventory()

    missing = inventory.validate_products_against_list(products_list)
    assert not missing, f"Missing products: {missing}"

    for product in products_list:
        inventory.add_product_to_cart_by_name(product)
    assert inventory.get_cart_count() == len(products_list)

    cart = CartPage(page)
    cart.open_cart()
    cart_items = cart.get_cart_item_names()
    for product in products_list:
        assert product in cart_items
        
    cart.proceed_to_checkout()
    checkout = CheckoutPage(page)
    # Using the config fixture
    checkout.fill_customer_info(
    config["customer_info"]["first"],
    config["customer_info"]["last"],
    config["customer_info"]["postal"])
    checkout.finish_checkout()
    confirmation = checkout.get_confirmation_text()
    assert confirmation and "THANK YOU" in confirmation.upper()
