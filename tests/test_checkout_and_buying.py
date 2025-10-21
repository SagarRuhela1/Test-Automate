from pages.checkout_page import CheckoutPage
from pages.adding_to_cart import AddingToCart
from pages.cart_page import CartPage

def test_checkout_backpack_and_buying(page, config):
    cart = AddingToCart(page)
    cart_page = CartPage(page)
    checkout = CheckoutPage(page)

    page.goto(config["inventory_url"], wait_until="networkidle")
    cart.add_backpack()
    cart.go_to_cart()

    cart_page.proceed_to_checkout()
    checkout.fill_customer_info(
    config["customer_info"]["first"],
    config["customer_info"]["last"],
    config["customer_info"]["postal"])
    checkout.continue_button.click()
    page.wait_for_load_state("networkidle")
    checkout.finish_checkout()
    confirmation_text = checkout.get_confirmation_text()
    assert confirmation_text == "Thank you for your order!"
