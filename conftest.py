import pytest
from playwright.sync_api import sync_playwright,expect
from pages.login_page import LoginPage
import os

@pytest.fixture(scope="session")
def browser_context(playwright):
    # device=playwright.devices["iPhone SE"]
    browser= playwright.chromium.launch(headless=True)
    #context=browser.new_context(**device)
    context=browser.new_context()
    page =context.new_page()
    login_page=LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.fillUserName("standard_user")
    login_page.fillPassword("secret_sauce")
    login_page.clickLoginBtn()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")

    context.storage_state(path="state.json")
    yield context
    context.close()
    browser.close()

@pytest.fixture
def page(browser_context, browser):
    # Create a new page using new browser but with same session
    # i am doing this so we can the test in parallel
    context=browser.new_context(storage_state="state.json")
    page=context.new_page()
    yield page
    page.close()


# Ensure screenshot folder exists
os.makedirs("reports/screenshots", exist_ok=True)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        page = item.funcargs.get("page", None)
        if page:
            safe_name = item.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")
            screenshot_path = f"reports/screenshots/{safe_name}.png"
            page.screenshot(path=screenshot_path, full_page=True)

            # Attach to HTML report
            if hasattr(report, "extra"):
                extra = report.extra
            else:
                extra = []

            try:
                import pytest_html
                html = f'<div><img src="screenshots/{safe_name}.png" alt="screenshot" style="width:600px;height:auto;" onclick="window.open(this.src)"/></div>'
                extra.append(pytest_html.extras.html(html))
                report.extra = extra
            except ImportError:
                pass