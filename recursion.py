def fib(n):
    """
    Recursively calculate the Fibonacci Sequence

    fib(4) -> 5
    """
    if n <= 2:
        return 1
    
    return fib(n - 2) + fib(n - 1)

def mul(x, y):
    """
    Multiply x by y without using * and the mul() function

    mul(2, 2) -> 4
    """
    if y == 1:
        return x
    return x + mul(x, y - 1)

def strictlyInc(x):
    """
    Return true if the integers from right to left are in a increasing fashion. Otherwise, return false

    >>> strictlyInc(652)
    True

    >>> strictlyInc(12)
    False
    """
    if x // 10 == 0:
        return True
    elif x % 10 > x // 10 % 10:
        return False
    return strictlyInc(x // 10)

def paths2D(x, y):
    """
    >>> paths2D(3, 2)
    10
    """

    if x == 0 or y == 0:
        return 1
    else:
        return paths2D(x - 1, y) + paths2D(x, y - 1)

def decrement_at(vector, i):
    vector = vector[:]
    vector[i] -= 1
    return vector

def pathND(vector):
    """
    >>> pathND([3, 2])
    10
    >>> pathND([3, 1, 2])
    60
    """

    if sum(vector) == 0:
        return 1
    else:
        return sum([pathND(decrement_at(vector, i)) for i in range(len(vector)) if vector[i] > 0])

if __name__ == "__main__":
    import doctest
    doctest.testmod()