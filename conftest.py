# this will run as a first file for pytest and fixture will be taken from here

import pytest
from django.contrib.auth.models import User


@pytest.fixture()
def user_2(db):
    print('Execution from conftest')
    user2 = User.objects.create_user("test_user2")
    return user2
