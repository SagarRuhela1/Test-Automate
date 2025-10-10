from playwright.sync_api import Page

class LogoutPage:
    def __init__(self, page:Page):
        self.menu= page.get_by_role("button", name="Open Menu")
        self.logout_Button=page.get_by_role("link", name="Logout")

    def openMenu(self):
        self.menu.click()        

    def clickLogoutBtn(self):
        self.logout_Button.click()