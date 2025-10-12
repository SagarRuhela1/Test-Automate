from playwright.sync_api import expect
from pages.adding_to_cart import AddingToCart

def test_add_items_to_cart(page):
    cart = AddingToCart(page)
    page.goto("https://www.saucedemo.com/inventory.html")
    cart.add_backpack()
    cart.add_bike()
    cart.go_to_cart()
    expect(cart.backpack_name_in_cart).to_contain_text("Sauce Labs Backpack")
    expect(cart.bike_name_in_cart).to_contain_text("Sauce Labs Bike Light")


def test_remove_items_from_cart(page):
    cart = AddingToCart(page)
    page.goto("https://www.saucedemo.com/inventory.html")
    cart.add_backpack()
    cart.add_bike()
    cart.go_to_cart()
    cart.remove_bike()
    cart.remove_backpack()
    expect(cart.backpack_name_in_cart).to_have_count(0)
    expect(cart.bike_name_in_cart).to_have_count(0)
