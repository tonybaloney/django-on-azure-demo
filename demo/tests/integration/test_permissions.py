from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse
import pytest


ANON_VIEWS_CHECK = [
    '/products/',
    '/products/1'
]


@pytest.mark.parametrize('path', ANON_VIEWS_CHECK)
@pytest.mark.django_db
def test_anonymous_categories_redirects_to_login(client, path):
    response = client.get(path)
    assert isinstance(response, HttpResponseRedirect)
    assert response.url.startswith("/login")


USERS_ALLOWED = [
    '/products/',
    '/products/1'
]


@pytest.mark.parametrize('path', USERS_ALLOWED)
@pytest.mark.django_db
def test_users_allowed(user_client, path):
    response = user_client.get(path)
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert "cheese" in response.content
