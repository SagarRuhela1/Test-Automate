from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_button = page.locator(".shopping_cart_link")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.cart_items = page.locator(".cart_item")
        self.item_name_locator = ".inventory_item_name"

    def open_cart(self):
        self.cart_button.click()
        self.page.wait_for_load_state("networkidle")

    def get_cart_item_names(self):
        return [item.locator(self.item_name_locator).inner_text().strip() for item in self.cart_items.all()]

    def proceed_to_checkout(self):
        if not self.checkout_button.is_visible():
            raise AssertionError("Checkout button not visible in cart")
        self.checkout_button.click()
        self.page.wait_for_load_state("networkidle")
