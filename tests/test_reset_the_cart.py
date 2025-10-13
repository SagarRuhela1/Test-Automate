from pages.reset_app_state import ResetAppState

def test_reset_app_state_functionality(page):
    reset_page = ResetAppState(page)
    page.goto("https://www.saucedemo.com/inventory.html", wait_until="networkidle")
    reset_page.add_items_to_cart()
    reset_page.open_menu()
    reset_page.reset_app_state()
    reset_page.open_cart()
    reset_page.verify_cart_is_empty()
