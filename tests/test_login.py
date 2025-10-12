import re
from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage

def test_login_user(page):
    login_page=LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    page.wait_for_timeout(2000)
    login_page.fillUserName("standard_user")
    login_page.fillPassword("secret_sauce")
    login_page.clickLoginBtn()
    page.wait_for_timeout(2000)
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")




    