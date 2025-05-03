import pytest

#sample test ---------------------------------
@pytest.fixture
def sample_date():
    return {"name" : "Serdar", "age" : 30}

def test_sample_test(sample_date):
    assert sample_date["name"] == "Serdar"

@pytest.fixture
def user():
    return {"username" : "Serdar", "role" : "QA Engineer", "age" : 30}

def test_user(user):
    assert user["username"] == "Serdar"

def test_user_role(user):
    assert user["role"] == "QA Engineer"

def test_user_age(user):
    assert user["age"] == 30