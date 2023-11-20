import calculator

def test_calculator_functions():
    """
    Test for calculator functions.
    """
    assert calculator.add(5, 3) == 8, "add should return 8 for add(5, 3)"
    assert calculator.subtract(5, 3) == 2, "subtract should return 2 for subtract(5, 3)"
    assert calculator.multiply(5, 3) == 15, "multiply should return 15 for multiply(5, 3)"
    assert calculator.divide(6, 3) == 2, "divide should return 2 for divide(6, 3)"
    assert calculator.divide(5, 0) == 'Division by zero', "divide should handle division by zero"
    assert calculator.power(2, 3) == 8, "power should return 8 for power(2, 3)"
    assert calculator.root(27, 3) == 3, "root should return 3 for root(27, 3)"
    assert calculator.root(16, 0) == 'Root by zero', "root should handle root by zero"