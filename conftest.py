import yaml, csv, pytest
from pathlib import Path
from playwright.sync_api import expect

ROOT = Path(__file__).parent

@pytest.fixture(scope="session")
def config():
    with open(ROOT / "config.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def products_list():
    with open(ROOT / "products.csv") as f:
        return [line.strip() for line in f if line.strip()]

@pytest.fixture(scope="session")
def browser_context(playwright, config):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(config["base_url"], wait_until="networkidle")
    from pages.login_page import LoginPage
    LoginPage(page).login(config["credentials"]["valid"]["username"], config["credentials"]["valid"]["password"])
    expect(page.locator("[data-test='title']")).to_contain_text("Products")
    context.storage_state(path="state.json")
    yield context
    context.close()
    browser.close()

@pytest.fixture
def page(browser_context, browser):
    context = browser.new_context(storage_state="state.json")
    page = context.new_page()
    yield page
    page.close()



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

            try:
                import pytest_html
                html = f'<div><img src="screenshots/{safe_name}.png" ' \
                       f'alt="screenshot" style="width:600px;height:auto;" ' \
                       f'onclick="window.open(this.src)"/></div>'
                extras = getattr(report, "extras", [])
                extras.append(pytest_html.extras.html(html))
                report.extras = extras
            except ImportError:
                pass
