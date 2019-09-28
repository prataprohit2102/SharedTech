import pytest
import requests

from api_models.models import UserSchema, BASE_URL


@pytest.mark.parametrize("username, password", [
    ('user', 'password'),
    ('admin', 'password')
])
def test_login_user(username, password):
    login_url = BASE_URL + '/login'
    request_body = {"username": username, "password": password}
    response = requests.post(url=login_url, json=request_body)
    assert response.status_code == 200
    user = UserSchema().load(response.json())
    assert user.username == username


def test_add_movie(admin):
    pass
