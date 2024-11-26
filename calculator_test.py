import inspect
from calculator import add, subtract, multiply, divide, power, root

def test_add():
    """
    Test for add function in calculator.
    """
    assert add(5, 3) == 8, "add should return 8 for add(5, 3)"

def test_subtract():
    """
    Test for subtract function in calculator.
    """
    assert subtract(5, 3) == 2, "subtract should return 2 for subtract(5, 3)"

def test_multiply():
    """
    Test for multiply function in calculator.
    """
    assert multiply(5, 3) == 15, "multiply should return 15 for multiply(5, 3)"

def test_divide():
    """
    Test for divide function in calculator.
    """
    assert divide(6, 3) == 2, "divide should return 2 for divide(6, 3)"


def test_divide_by_zero():
    """
    Test for divide function in calculator.
    """
    assert divide(5, 0) == 'Division by zero', "divide should handle division by zero"


def test_power():
    """
    Test for power function in calculator.
    """
    assert power(2, 3) == 8, "power should return 8 for power(2, 3)"

def test_root():
    """
    Test for root function in calculator.
    """
    assert root(27, 3) == 3, "root should return 3 for root(27, 3)"


def test_zero_root():
    """
    Test for root function in calculator.
    """
    assert root(16, 0) == 'Root by zero', "root should handle root by zero"


def test_docstring_add():
    docstring = inspect.getdoc(add)
    assert docstring is not None, "Docstring fehlt in der Funktion 'add'"

    params = inspect.signature(add).parameters
    for param in params:
        assert f":param {param}:" in docstring, f"Docstring fehlt :param für {param} in 'add'"

    assert ":return:" in docstring, "Docstring fehlt :return in 'add'"


def test_docstring_subtract():
    docstring = inspect.getdoc(subtract)
    assert docstring is not None, "Docstring fehlt in der Funktion 'subtract'"

    params = inspect.signature(subtract).parameters
    for param in params:
        assert f":param {param}:" in docstring, f"Docstring fehlt :param für {param} in 'subtract'"

    assert ":return:" in docstring, "Docstring fehlt :return in 'subtract'"


def test_docstring_multiply():
    docstring = inspect.getdoc(multiply)
    assert docstring is not None, "Docstring fehlt in der Funktion 'multiply'"

    params = inspect.signature(multiply).parameters
    for param in params:
        assert f":param {param}:" in docstring, f"Docstring fehlt :param für {param} in 'multiply'"

    assert ":return:" in docstring, "Docstring fehlt :return in 'multiply'"


def test_docstring_divide():
    docstring = inspect.getdoc(divide)
    assert docstring is not None, "Docstring fehlt in der Funktion 'divide'"

    params = inspect.signature(divide).parameters
    for param in params:
        assert f":param {param}:" in docstring, f"Docstring fehlt :param für {param} in 'divide'"

    assert ":return:" in docstring, "Docstring fehlt :return in 'divide'"


def test_docstring_power():
    docstring = inspect.getdoc(power)
    assert docstring is not None, "Docstring fehlt in der Funktion 'power'"

    params = inspect.signature(power).parameters
    for param in params:
        assert f":param {param}:" in docstring, f"Docstring fehlt :param für {param} in 'power'"

    assert ":return:" in docstring, "Docstring fehlt :return in 'power'"


def test_docstring_root():
    docstring = inspect.getdoc(root)
    assert docstring is not None, "Docstring fehlt in der Funktion 'root'"

    params = inspect.signature(root).parameters
    for param in params:
        assert f":param {param}:" in docstring, f"Docstring fehlt :param für {param} in 'root'"

    assert ":return:" in docstring, "Docstring fehlt :return in 'root'"