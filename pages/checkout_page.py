from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.locator("[data-test='firstName']")
        self.last_name = page.locator("[data-test='lastName']")
        self.postal_code = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.finish_button = page.locator("[data-test='finish']")
        self.confirmation_header = page.locator(".complete-header")

    def fill_customer_info(self, first="John", last="Doe", postal="12345"):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)


    def finish_checkout(self):
        if not self.finish_button.is_visible():
            raise AssertionError("Finish button not visible")
        self.finish_button.click()
        self.page.wait_for_load_state("networkidle")

    def get_confirmation_text(self):
        if self.confirmation_header.is_visible():
            return self.confirmation_header.inner_text().strip()
        return None
