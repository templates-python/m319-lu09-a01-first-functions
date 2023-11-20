def function1():
    """
    Function without params or return
    :return: None
    """
    print('Function 1 is called')


def function2():
    """
    Function without params, but returns a value
    :return: str
    """
    return 'Function 2 is called'


def function3(argument):
    """
    Function with a param and no return
    :param argument: str
    :return: None
    """
    print(f'Function 3 is called with argument: {argument}')


def function4(argument):
    """
    Function with a param and a return
    :param argument: str
    :return: str
    """
    return f'Function 4 is called with argument: {argument}'


def four_functions():
    """
    Main function
    :return: None
    """
    function1()
    received_from_2 = function2()
    print(received_from_2)
    function3('passed Argument to print in function3')
    received_from_4 = function4('passed Argument to print in function4')
    print(received_from_4)



if __name__ == '__main__':
    four_functions()
