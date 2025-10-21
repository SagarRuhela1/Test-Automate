import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.parametrize("cred_key, should_succeed", [("valid", True), ("invalid", False)])
def test_login_variants(page, config, cred_key, should_succeed):
    login = LoginPage(page)
    login.goto(config["base_url"])
    user = config["credentials"][cred_key]["username"]
    pwd = config["credentials"][cred_key]["password"]
    login.login(user, pwd)

    if should_succeed:
        InventoryPage(page).assert_on_inventory()
    else:
        err = login.get_error_message()
        assert err, "Expected error for invalid login"
