# test_inventory_page.py
from playwright.sync_api import expect
from pages.inventory_page import InventoryPage


def test_inventory_page_loads(page, config):
    inventory = InventoryPage(page)
    page.goto(config["inventory_url"], wait_until="networkidle")

    # Verify you are on the inventory page
    inventory.assert_on_inventory()
    expect(page).to_have_url(config["inventory_url"])


def test_add_product_to_cart(page, config):
    inventory = InventoryPage(page)
    page.goto(config["inventory_url"], wait_until="networkidle")
    inventory.add_product_to_cart_by_name("Sauce Labs Backpack")
    count = inventory.get_cart_count()
    assert count == 1, f"Expected cart count 1, got {count}"


def test_validate_products_on_page(page, config,products_list):
    inventory = InventoryPage(page)
    page.goto(config["inventory_url"], wait_until="networkidle")
    missing = inventory.validate_products_against_list(products_list)
    assert not missing, f"Missing products: {missing}"
