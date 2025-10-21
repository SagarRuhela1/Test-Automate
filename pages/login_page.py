from playwright.sync_api import Page, TimeoutError

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_container = page.locator("[data-test='error']")

    def goto(self, base_url: str):
        self.page.goto(base_url, wait_until="networkidle")

    def login(self, username: str, password: str, timeout: int = 5000):
        try:
            self.username_input.fill(username, timeout=timeout)
            self.password_input.fill(password, timeout=timeout)
            self.login_button.click()
            self.page.wait_for_load_state("networkidle")
        except TimeoutError as e:
            raise RuntimeError("Timeout while trying to perform login") from e

    def get_error_message(self):
        try:
            if self.error_container.is_visible():
                return self.error_container.inner_text()
        except Exception:
            return None
        return None

    def assert_logged_in(self):
        title = self.page.locator("[data-test='title']")
        if not title.is_visible(timeout=3000):
            raise AssertionError("Login did not succeed - 'Products' title not visible")
