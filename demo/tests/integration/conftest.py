import pytest
from django.core.management import call_command


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'data/test.json')


@pytest.fixture
def user_client(client, django_user_model):
    username = "user1"
    _pw = "barbarblacksheep"
    django_user_model.objects.create_user(username=username, password=_pw)
    client.login(username=username, password=_pw)
    return client
