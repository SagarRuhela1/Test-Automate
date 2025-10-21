# test_reset_app_state.py
from pages.reset_app_state import ResetAppState
from playwright.sync_api import expect

def test_reset_app_state_functionality(page, config):
    reset_page = ResetAppState(page)
    page.goto(config["inventory_url"], wait_until="networkidle")
    reset_page.add_items_to_cart()
    reset_page.open_menu()
    reset_page.reset_app_state()
    reset_page.open_cart()
    reset_page.verify_cart_is_empty()
