import pytest

from api_models.models import User


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.binary = '/path/to/firefox-bin'
    firefox_options.add_argument('-foreground')
    firefox_options.set_preference('browser.anchor_color', '#FF0000')
    return firefox_options


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    return chrome_options


@pytest.fixture()
def admin():
    user = User.login('admin', 'password')
    return user
