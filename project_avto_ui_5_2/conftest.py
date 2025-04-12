import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='session')
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    yield browser

    browser.close()
    playwright.stop()
