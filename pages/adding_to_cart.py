from playwright.sync_api import Page

class AddingToCart:
    def __init__(self, page: Page):
        self.page = page
        self.item_backpack_add = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.item_bike_add = page.locator("[data-test='add-to-cart-sauce-labs-bike-light']")
        self.item_backpack_remove = page.locator("[data-test='remove-sauce-labs-backpack']")
        self.item_bike_remove = page.locator("[data-test='remove-sauce-labs-bike-light']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")
        self.backpack_name_in_cart = page.locator("[data-test='item-4-title-link'] [data-test='inventory-item-name']")
        self.bike_name_in_cart = page.locator("[data-test='item-0-title-link'] [data-test='inventory-item-name']")

    def add_backpack(self):
        self.item_backpack_add.click()

    def add_bike(self):
        self.item_bike_add.click()

    def remove_backpack(self):
        self.item_backpack_remove.click()

    def remove_bike(self):
        self.item_bike_remove.click()

    def go_to_cart(self):
        self.cart_link.click()
