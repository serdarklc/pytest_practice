import pytest

@pytest.fixture
def connect_db():
    print("DB Connection")
    yield "DB Object"
    print("DB Disconnect")

def test_query_1(connect_db):
    print(f"Query 1 : {connect_db}")

def test_query_2(connect_db):
    print(f"Query 2 : {connect_db}")