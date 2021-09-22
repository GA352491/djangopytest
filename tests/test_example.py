import pytest
from django.contrib.auth.models import User


# Arrange
# Act
# Assert

@pytest.fixture
def fixture1():
    print('run-fixture-1')
    return 1


def test_example(fixture1):
    num = fixture1
    assert num == 1


@pytest.mark.django_db
def test_db():
    User.objects.create(email='t@t.com', last_name='sample')
    count = User.objects.all().count()
    print(count)
    assert count == 1


@pytest.mark.django_db
def test_db1():
    count = User.objects.all().count()
    print(count)
    assert count == 0


@pytest.fixture()
def user_1(db):
    return User.objects.create_user("test_user")


@pytest.mark.django_db
def test_set_check_password(user_1):
    print(user_1)
    user_1.set_password("new-password")
    assert user_1.check_password("new-password") is True


# @pytest.fixture(scope='session') only used once
# @pytest.fixture()
# def user_2(db):
#     user2 = User.objects.create_user("test_user2")
#     return user2


def test_set_check_password2(user_2):
    print(user_2)
    assert user_2.username == 'test_user2'
