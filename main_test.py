import main

def test_function1():
    """
    Test for unction1
    """
    # Since function1 only prints, we just test if it runs without errors
    main.function1()

def test_function2():
    """
    Test for function2
    """
    assert main.function2() == 'Function 2 is called', "function2 should return 'Function 2 is called'"

def test_function3():
    """
    Test for function3
    """
    # Since function3 only prints, we test if it runs without errors
    main.function3('test')

def test_function4():
    """
    Test for function4
    :return: None
    """
    # Testing with different arguments and ensuring that the return value is not None
    assert main.function4('test') is not None, "function4 should return a non-None value for 'test'"
