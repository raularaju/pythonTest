import pytest
from mymath import MyMath  # Assuming your class is saved in a file named `mymath.py`

# Create an instance of MyMath to use in the tests
math = MyMath()

def test_add():
  assert math.add(2, 3) == 5
  assert math.add(-1, 1) == 0
  assert math.add(0, 0) == 0

def test_subtract():
  assert math.subtract(10, 5) == 5
  assert math.subtract(0, 5) == -5
  assert math.subtract(-5, -5) == 0

def test_multiply():
  assert math.multiply(4, 5) == 20
  assert math.multiply(0, 5) == 0
  assert math.multiply(-3, 3) == -9

def test_divide():
  assert math.divide(10, 2) == 5
  assert math.divide(-10, 2) == -5
  assert math.divide(0, 1) == 0

  with pytest.raises(ValueError, match="Cannot divide by zero"):
      math.divide(10, 0)

def test_power():
    assert math.power(2, 3) == 8
    assert math.power(5, 0) == 1
    assert math.power(3, -2) == 1/9

def test_square_root():
    assert math.square_root(4) == 2
    assert math.square_root(0) == 0
    assert math.square_root(9) == 3

    with pytest.raises(ValueError, match="Cannot compute square root of negative number"):
        math.square_root(-1)