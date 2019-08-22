import pytest

@pytest.fixture(scope="session", autouse=True)
def setupSession2():
    print("\nSetup Session2")

@pytest.fixture(scope="module", autouse=True)
def setupModule2():
    print("\nSetup Module2")

@pytest.fixture(scope="function", autouse=True)
def setupFunction2():
    print("\nSetup Function2")

def test1():
    print("Execurting test1")
    assert True

def test2():
    print("Execurting test2")
    assert True
