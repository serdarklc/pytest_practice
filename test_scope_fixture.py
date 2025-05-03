import pytest

@pytest.fixture
def hello():
    print("👋 Merhaba!")
    return "selam"

def test_one(hello):
    print(f"Test 1: {hello}")

def test_two(hello):
    print(f"Test 2: {hello}")


@pytest.fixture(scope="module") # İlk seferinde çalışır devamındaki çağırmalarda return kısmı döner sadece 
def hello2():
    print("👋 Merhaba!")
    return "selam"

def test_three(hello2):
    print(f"Test 3: {hello2}")

def test_four(hello2):
    print(f"Test 4: {hello2}")
