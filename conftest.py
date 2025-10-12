import pytest
from playwright.sync_api import sync_playwright,expect
from pages.login_page import LoginPage

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

