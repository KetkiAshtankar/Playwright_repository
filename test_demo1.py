import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    #Given I am on saucedemo login page
    page.goto("https://www.saucedemo.com/")
    expect(page.locator("[data-test=\"username\"]")).to_be_visible()
    expect(page.locator("[data-test=\"password\"]")).to_be_visible()
    #When I login with valid credentials 
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    #Then I should see the homepage with title "Swag Labs"
    expect(page.locator("[data-test=\"primary-header\"]")).to_contain_text("Swag Labs")


# AAA (Arrange, Act, Assert)
# Given, When, Then (BDD)




