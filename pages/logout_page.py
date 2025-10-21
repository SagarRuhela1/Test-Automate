from playwright.sync_api import Page

class LogoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.logout_link = page.locator("[data-test='logout-sidebar-link']")
        self.login_button = page.locator("[data-test='login-button']")

    def open_menu(self):
        self.menu_button.click()

    def click_logout(self):
        self.logout_link.click()
