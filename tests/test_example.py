import pytest
from playwright.sync_api import Page

from static.settings import get_settings, Settings

settings: Settings = get_settings()

def test_example_page_title(page: Page, sample_fixture):
    print(f"Using fixture: {sample_fixture}")
    page.goto(settings.BASE_URL)
    assert "Playwright" in page.title() 