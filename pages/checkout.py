from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.selectBackpack = page.locator("[data-test='item-4-title-link']")
        self.itemName = page.locator("[data-test='inventory-item-name']")
        self.addToCartBtn = page.locator("[data-test='add-to-cart']")
        self.cartBtn = page.locator("[data-test='shopping-cart-link']")
        self.checkoutBtn = page.locator("[data-test='checkout']")
        self.firstNameInput = page.locator("[data-test='firstName']")
        self.lastNameInput = page.locator("[data-test='lastName']")
        self.postalCodeInput = page.locator("[data-test='postalCode']")
        self.continueBtn = page.locator("[data-test='continue']")
        self.checkoutTitle = page.locator("[data-test='title']")
        self.priceTotalLabel = page.locator("[data-test='total-info-label']")
        self.finishBtn = page.locator("[data-test='finish']")
        self.orderCompleteHeader = page.locator("[data-test='complete-header']")
        self.backToProductsBtn = page.locator("[data-test='back-to-products']")

    def select_backpack_item(self):
        self.selectBackpack.click()

    def verify_product_detail(self):
        return self.itemName

    def add_to_cart(self):
        self.addToCartBtn.click()

    def go_to_cart(self):
        self.cartBtn.click()

    def proceed_to_checkout(self):
        self.checkoutBtn.click()

    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str):
        self.firstNameInput.fill(first_name)
        self.lastNameInput.fill(last_name)
        self.postalCodeInput.fill(postal_code)

    def continue_checkout(self):
        self.continueBtn.click()

    def finish_checkout(self):
        self.finishBtn.click()

    def go_back_to_products(self):
        self.backToProductsBtn.click()
