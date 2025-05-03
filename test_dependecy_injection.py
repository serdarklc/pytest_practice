import pytest


@pytest.fixture
def db_connection():
    return "DB Connection"

@pytest.fixture
def db_query(db_connection):
    return f"DB Query : {db_connection}"

def test_db_query(db_query):
    assert "Connection" in db_query