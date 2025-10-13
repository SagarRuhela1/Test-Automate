from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page:Page):
        self.userNameInput= page.locator("[data-test=\"username\"]")
        self.passwordInput=page.locator("[data-test=\"password\"]")
        self.login_Button=page.locator("[data-test=\"login-button\"]")
        self.main_page_title=page.locator("[data-test=\"title\"]")

    def fillUserName(self, userName:str):
        self.userNameInput.fill(userName)    
    def fillPassword(self,password):
        self.passwordInput.fill(password)
    def clickLoginBtn(self):
        self.login_Button.click()
