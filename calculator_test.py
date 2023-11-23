import calculator

def test_add():
    """
    Test for add function in calculator.
    """
    assert calculator.add(5, 3) == 8, "add should return 8 for add(5, 3)"

def test_subtract():
    """
    Test for subtract function in calculator.
    """
    assert calculator.subtract(5, 3) == 2, "subtract should return 2 for subtract(5, 3)"

def test_multiply():
    """
    Test for multiply function in calculator.
    """
    assert calculator.multiply(5, 3) == 15, "multiply should return 15 for multiply(5, 3)"

def test_divide():
    """
    Test for divide function in calculator.
    """
    assert calculator.divide(6, 3) == 2, "divide should return 2 for divide(6, 3)"


def test_divide_by_zero():
    """
    Test for divide function in calculator.
    """
    assert calculator.divide(5, 0) == 'Division by zero', "divide should handle division by zero"


def test_power():
    """
    Test for power function in calculator.
    """
    assert calculator.power(2, 3) == 8, "power should return 8 for power(2, 3)"

def test_root():
    """
    Test for root function in calculator.
    """
    assert calculator.root(27, 3) == 3, "root should return 3 for root(27, 3)"


def test_zero_root():
    """
    Test for root function in calculator.
    """
    assert calculator.root(16, 0) == 'Root by zero', "root should handle root by zero"