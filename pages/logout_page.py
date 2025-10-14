from playwright.sync_api import Page

class LogoutPage:
    def __init__(self, page:Page):
        self.menu= page.get_by_role("button", name="Open Menu")
        self.logout_button=page.get_by_role("link", name="Logout")
        self.login_button=page.locator("[data-test=\"login-button\"]")
        print()

    def openMenu(self):
        self.menu.click()        

    def clickLogoutBtn(self):
        self.logout_button.click()