import pytest


@pytest.fixture(autouse=True)
def announce():
    print("\n Test is starting")

def test_one():
    print("Test 1")

def test_two():
    print("Test 2")

def test_three():
    print("Test 3")

