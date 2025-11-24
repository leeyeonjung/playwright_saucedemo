# tests/conftest.py
from pathlib import Path
from datetime import datetime

import pytest
from playwright.sync_api import sync_playwright


def pytest_configure(config):
    """pytest 설정 시 실행 날짜를 메타데이터에 추가
    
    Args:
        config: pytest 설정 객체
    """
    now = datetime.now()
    execution_date = now.strftime("%Y-%m-%d %H:%M:%S")
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

    metadata = getattr(config, "_metadata", None)
    if metadata is not None:
        metadata["Execution Date"] = execution_date
        metadata["title"] = f"Sauce Demo Test Report - {execution_date}"

    report_dir = Path("tests") / "Results"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / f"report_{timestamp}.html"
    config.option.htmlpath = str(report_path)


@pytest.fixture(scope="session")
def playwright_instance():
    """Playwright 인스턴스 생성 및 관리
    
    Yields:
        playwright: Playwright 인스턴스
    """
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance):
    """브라우저 인스턴스 생성 및 관리
    
    Args:
        playwright_instance: Playwright 인스턴스
        
    Yields:
        browser: Chromium 브라우저 인스턴스 (headless=True로 브라우저 화면 숨김)
    """
    browser = playwright_instance.chromium.launch(headless=True)  # headless=True로 변경하여 브라우저 화면 숨김
    yield browser
    browser.close()


@pytest.fixture
def page(browser):
    """테스트용 페이지 인스턴스 생성 및 관리
    
    Args:
        browser: 브라우저 인스턴스
        
    Yields:
        page: Playwright 페이지 객체 (base_url: https://www.saucedemo.com)
    """
    context = browser.new_context(base_url="https://www.saucedemo.com")
    page = context.new_page()
    yield page
    context.close()

