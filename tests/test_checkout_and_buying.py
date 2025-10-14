from playwright.sync_api import  expect
from playwright.sync_api import expect
from pages.checkout import CheckoutPage

def test_checkout_backpack_and_buying(page):
    checkout = CheckoutPage(page)
    page.goto("https://www.saucedemo.com/inventory.html", wait_until="networkidle")
    checkout.select_backpack_item()
    expect(checkout.verify_product_detail()).to_contain_text("Sauce Labs Backpack")
    checkout.add_to_cart()
    checkout.go_to_cart()
    checkout.proceed_to_checkout()
    checkout.fill_checkout_form("test", "user", "12345")
    checkout.continue_checkout()
    expect(checkout.checkoutTitle).to_contain_text("Checkout: Overview")
    expect(checkout.priceTotalLabel).to_contain_text("Price Total")
    checkout.finish_checkout()
    expect(checkout.orderCompleteHeader).to_contain_text("Thank you for your order!")
    expect(checkout.backToProductsBtn).to_be_visible()
    checkout.go_back_to_products()
    print("test run successfully")
    expect(checkout.checkoutTitle).to_contain_text("Products")
