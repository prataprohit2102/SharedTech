import pytest

from base_element import HomePage


@pytest.mark.parametrize("username, password", [
    ('user', 'password'),
    ('admin', 'password')
])
def test_successful_login_to_the_application(selenium, username, password):
    homepage = HomePage(selenium)
    homepage.navigate()
    homepage.login(username, password)
    selenium.implicitly_wait(5)
    # assert homepage.verify_logout_exists() is True


@pytest.mark.parametrize("username, password", [
    ('jhguu', 'password')
])
def test_failed_login_to_the_application(selenium, username, password):
    homepage = HomePage(selenium)
    homepage.navigate()
    homepage.login(username, password)
    # assert homepage.verify_logout_exists() is False
