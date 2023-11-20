def add(x, y):
    """
    Add two numbers.
    :param x: Number
    :param y: Number
    :return: Sum of x and y
    """
    return x + y

def subtract(x, y):
    """
    Subtract y from x.
    :param x: Number
    :param y: Number
    :return: Difference of x and y
    """
    return x - y

def multiply(x, y):
    """
    Multiply x by y.
    :param x: Number
    :param y: Number
    :return: Product of x and y
    """
    return x * y

def divide(x, y):
    """
    Divide x by y.
    :param x: Number
    :param y: Number
    :return: Quotient of x and y
    """
    return x / y if y != 0 else 'Division by zero'

def power(x, y):
    """
    Calculate x raised to the power of y.
    :param x: Base number
    :param y: Exponent
    :return: x raised to the power of y
    """
    return x ** y

def root(x, y):
    """
    Calculate the y-th root of x.
    :param x: Number
    :param y: Root
    :return: y-th root of x
    """
    return x ** (1 / y) if y != 0 else 'Root by zero'

def main():
    print(add(5, 5.5))
    print(subtract(5, 3))
    print(multiply(5, 3))
    print(divide(6, 3))
    print(divide(5, 0))
    print(power(2, 3))
    print(root(27, 3))
    print(root(16, 0))


if __name__ == '__main__':
    main()