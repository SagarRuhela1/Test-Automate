from playwright.sync_api import Page, expect, TimeoutError

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.page_title = page.locator("[data-test='title']")
        self.inventory_items = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.item_name_locator = ".inventory_item_name"
        self.add_button_locator = "button.btn_inventory"

    def assert_on_inventory(self):
        try:
            expect(self.page_title).to_contain_text("Products")
        except TimeoutError:
            raise AssertionError("Not on inventory page - title mismatch")

    def get_all_product_names(self):
        names = []
        for el in self.inventory_items.all():
            try:
                names.append(el.locator(self.item_name_locator).inner_text().strip())
            except Exception:
                continue
        return names

    def add_product_to_cart_by_name(self, product_name: str):
        for card in self.inventory_items.all():
            try:
                name_el = card.locator(self.item_name_locator)
                if name_el.inner_text().strip() == product_name:
                    card.locator(self.add_button_locator).click()
                    return True
            except Exception:
                continue
        raise AssertionError(f"Product '{product_name}' not found on inventory page")

    def get_cart_count(self):
        if self.cart_badge.is_visible():
            return int(self.cart_badge.inner_text())
        return 0

    def validate_products_against_list(self, product_list):
        visible = self.get_all_product_names()
        missing = [p for p in product_list if p not in visible]
        return missing
