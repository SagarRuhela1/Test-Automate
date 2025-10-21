# test_about.py
from pages.about_page import AboutPage

def test_about_page_opening(page, config):
    about_page = AboutPage(page)
    page.goto(config["inventory_url"], wait_until="networkidle")
    about_page.open_menu()
    about_page.click_about_link()
    about_page.verify_about_page()
