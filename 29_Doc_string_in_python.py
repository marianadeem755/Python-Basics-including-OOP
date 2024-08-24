def square():
    '''By taking the square of n we get the multiplied number of the value with 2
    Hence This is the python doc str literal'''
n=50
print(n*2)
print(square.__doc__)

def number():
    '''What is your score in test . can you please tell me.
    It can be printed by using doc str literal of python'''
n=1000
print(n*2)
print(number.__doc__)

import this
def add(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2


def add(num1, num2):
    '''
    Firstly we take the num1 which is 98, Then we take the num2 which is 56
    The First operation we perform on it is the addition and then Subtraction, Multiplication and then division.
    Then we print the doc string'''
num1=98
num2=56
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(add.__doc__)# last pai doc kai bad dot(.) nhi ana