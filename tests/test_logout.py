import re
from playwright.sync_api import sync_playwright, expect

def test_logout_functionality(page):
     page.goto("https://www.saucedemo.com/inventory.html")
     page.get_by_role("button", name="Open Menu").click()
     page.locator("[data-test=\"logout-sidebar-link\"]").click()
     expect(page.locator("[data-test=\"login-button\"]")).to_be_visible()
     print("Logout succesfully")