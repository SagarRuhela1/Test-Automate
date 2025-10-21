from playwright.sync_api import expect
from pages.logout_page import LogoutPage

def test_logout_functionality(page, config):
    logout_page = LogoutPage(page)
    page.goto(config["inventory_url"], wait_until="networkidle")
    logout_page.open_menu()
    logout_page.click_logout()
    expect(logout_page.login_button).to_be_visible()
