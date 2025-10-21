from playwright.sync_api import Page

class AddingToCart:
    def __init__(self, page: Page):
        self.page = page
        self.backpack_add_btn = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.bike_add_btn = page.locator("[data-test='add-to-cart-sauce-labs-bike-light']")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.backpack_remove_btn = page.locator("[data-test='remove-sauce-labs-backpack']")
        self.bike_remove_btn = page.locator("[data-test='remove-sauce-labs-bike-light']")
        self.backpack_name_in_cart = page.locator(".inventory_item_name", has_text="Sauce Labs Backpack")
        self.bike_name_in_cart = page.locator(".inventory_item_name", has_text="Sauce Labs Bike Light")

    def add_backpack(self):
        self.backpack_add_btn.click()

    def add_bike(self):
        self.bike_add_btn.click()

    def go_to_cart(self):
        self.cart_icon.click()
        self.page.wait_for_load_state("networkidle")

    def remove_backpack(self):
        if self.backpack_remove_btn.is_visible():
            self.backpack_remove_btn.click()

    def remove_bike(self):
        if self.bike_remove_btn.is_visible():
            self.bike_remove_btn.click()
