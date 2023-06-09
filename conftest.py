import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_url():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1200
    browser.config.window_width = 1500

    pass
