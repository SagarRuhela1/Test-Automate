from playwright.sync_api import Page, expect

class ResetAppState:
    def __init__(self, page: Page):
        self.page = page
        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.reset_link = page.locator("[data-test='reset-sidebar-link']")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.add_backpack = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.add_bike = page.locator("[data-test='add-to-cart-sauce-labs-bike-light']")
        self.cart_items = page.locator(".cart_item")

    def add_items_to_cart(self):
        self.add_backpack.click()
        self.add_bike.click()

    def open_menu(self):
        self.menu_button.click()

    def reset_app_state(self):
        self.reset_link.click()

    def open_cart(self):
        self.cart_icon.click()

    def verify_cart_is_empty(self):
        expect(self.cart_items).to_have_count(0)
