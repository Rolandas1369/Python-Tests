import pytest

@pytest.fixture()
def setup1():
    print("\nSetup 1")
    yield
    print("\nTeardown 1")

@pytest.fixture()
def setup2(request):
    print("\nSetup 2")

    def teardown_a():
        print("\nTeardown A")

    def teardown_b():
        print("\nTeardown B")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)
