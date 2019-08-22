import pytest
import FizzBuzzTest

# 3 stages of testing 1. Create fail test 2. Refactor 3. Update code
# def test_canCallFizzBuzz():
#     FizzBuzzTest.fizzBuzz(1)


# def test_canAssertTrue():
#     assert True

# def test_returns1WithPassedIn():
#     retVal = FizzBuzzTest.fizzBuzz(1)
#     assert retVal == "1"

## more general way
def test_returns1WithPassedIn():
    FizzBuzzTest.checkFizzBuzz(1, "1")

# def test_returns2withPassed2():
#     retVal = FizzBuzzTest.fizzBuzz(2)
#     assert retVal == "2"

## more general way
def test_returns2WithPassedIn():
    FizzBuzzTest.checkFizzBuzz(2, "2")

def test_returnsFizzWithPassed3():
    FizzBuzzTest.checkFizzBuzz(3, "Fizz")

def test_returnsBuzzWithPassed5():
    FizzBuzzTest.checkFizzBuzz(5, "Buzz")

def test_Fizz_with6Passed():
    FizzBuzzTest.checkFizzBuzz(6, "Fizz")

def test_Buzz_with10Passed():
    FizzBuzzTest.checkFizzBuzz(10, "Buzz")

def test_returnFizzBuzzWuth15PassedIN():
    FizzBuzzTest.checkFizzBuzz(15, "FizzBuzz")


if __name__ == '__main__':
    pytest.main()