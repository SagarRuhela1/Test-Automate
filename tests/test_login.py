import re
from playwright.sync_api import sync_playwright, expect

def test_login_user(page):
    page.wait_for_timeout(3000)
    print("login succefull")


    