def function1():
    """
    Function without params or return
    :return: None
    """
    print('Function 1 is called')


def four_functions():
    """
    Main function
    :return: None
    """
    function1()
    received_from_2 = function2()
    function3('passed Argument to print in function3')
    received_from_4 = function4('passed Argument to print in function4')


if __name__ == '__main__':
    four_functions()