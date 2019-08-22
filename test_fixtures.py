import pytest

@pytest.fixture(autouse=True)
def setup():
    print("\nSetup")

#can pass functions as params to run before
#def test1(setup):

def test1():
    print("Execurting test1!")
    assert True

#@pytest.mark.usefixtures("setup")
def test2():
    print("Execurting test2!")
    assert True
