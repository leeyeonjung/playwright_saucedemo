# tests/testcases/test_login.py
from pytest_check import check

from tests.src.actions.login_actions import LoginActions


def test_login_success(page):
    """정상 로그인 테스트"""
    login = LoginActions(page)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory_title = login.get_inventory_title()
    check.equal(inventory_title, "Products", "Inventory title should match after login")


def test_login_failure_with_locked_out_user(page):
    """잠긴 계정 로그인 실패 테스트"""
    login = LoginActions(page)
    login.load()
    login.login("locked_out_user", "secret_sauce")

    error_text = login.get_error_message()
    check.equal(
        "Epic sadface: Sorry, this user has been locked out.", error_text, "Error message mismatch"
    )


def test_login_failure_with_wrong_password(page):
    """잘못된 비밀번호로 로그인 실패 테스트"""
    login = LoginActions(page)
    login.load()
    login.login("standard_user", "wrong_password")

    error_text = login.get_error_message()
    check.equal(
        "Epic sadface: Username and password do not match any user in this service",
        error_text,
        "Error message should indicate wrong credentials"
    )


def test_login_failure_with_wrong_username(page):
    """잘못된 사용자명으로 로그인 실패 테스트"""
    login = LoginActions(page)
    login.load()
    login.login("wrong_user", "secret_sauce")

    error_text = login.get_error_message()
    check.equal(
        "Epic sadface: Username and password do not match any user in this service",
        error_text,
        "Error message should indicate wrong credentials"
    )


def test_login_failure_with_empty_credentials(page):
    """빈 자격증명으로 로그인 실패 테스트"""
    login = LoginActions(page)
    login.load()
    login.login("", "")

    error_text = login.get_error_message()
    check.equal(
        "Epic sadface: Username is required",
        error_text,
        "Error message should indicate username is required"
    )

