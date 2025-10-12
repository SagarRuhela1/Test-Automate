import re
from playwright.sync_api import sync_playwright, expect
from pages.logout_page import LogoutPage

def test_logout_functionality(page):
     logout_page=LogoutPage(page)
     page.goto("https://www.saucedemo.com/inventory.html")
     page.wait_for_timeout(2000)
     logout_page.openMenu()
     page.wait_for_timeout(2000)
     logout_page.clickLogoutBtn()
     
     