import pytest

from base_element import HomePage


@pytest.mark.parametrize("username, password", [
    ('user', 'password'),
    ('admin', 'password')
])
def test_login_to_the_application(selenium, username, password):
    homepage = HomePage(selenium)
    homepage.navigate()
    homepage.login(username, password)
