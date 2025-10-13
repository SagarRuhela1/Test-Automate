from playwright.sync_api import Page, expect

class ResetAppState:
    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.add_backpack_btn = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.add_bike_light_btn = page.locator("[data-test='add-to-cart-sauce-labs-bike-light']")
        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.reset_app_link = page.locator("[data-test='reset-sidebar-link']")
        self.cart_button = page.locator("[data-test='shopping-cart-link']")
        self.backpack_item = page.locator("[data-test='item-4-title-link'] [data-test='inventory-item-name']")
        self.bike_light_item = page.locator("[data-test='item-0-title-link'] [data-test='inventory-item-name']")

    # Actions
    def add_items_to_cart(self):
        self.add_backpack_btn.click()
        self.add_bike_light_btn.click()

    def open_menu(self):
        expect(self.menu_button).to_be_visible()
        self.menu_button.click()

    def reset_app_state(self):
        self.reset_app_link.click()

    def open_cart(self):
        self.cart_button.click()

    # Assertions
    def verify_cart_is_empty(self):
        expect(self.backpack_item).to_have_count(0)
        expect(self.bike_light_item).to_have_count(0)
