import re
from playwright.sync_api import sync_playwright, expect
from pages.logout_page import LogoutPage

def test_logout_functionality(page):
     logout_page=LogoutPage(page)
     page.goto("https://www.saucedemo.com/inventory.html", wait_until="networkidle")
     page.wait_for_timeout(2000)
     logout_page.openMenu()
     page.wait_for_timeout(2000)
     logout_page.clickLogoutBtn()
     expect(logout_page.login_button).to_be_visible()
     expect(logout_page.login_button).to_contain_text("Login")
     
     