from playwright.sync_api import Page, expect

class AboutPage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.about_link = page.locator("[data-test='about-sidebar-link']")
        self.header_text = page.locator("h1")

    def open_menu(self):
        self.menu_button.click()

    def click_about_link(self):
        self.about_link.wait_for(state="visible")
        self.about_link.click()

    def verify_about_page(self):
        expect(self.header_text).to_contain_text("Build apps users love with AI-driven quality")
