def sum(n):
    """Computes the sum of all integers between 1 and n, inclusive.
    Assume n is positive.

    >>> sum(1)
    1
    >>> sum(5)  # 1 + 2 + 3 + 4 + 5
    15
    """
    if n == 1:
        return 1
    return n + sum(n-1)

def sine(x):
    if x < 0.0001:
        return x
    
    return 3*sine(x/3) - 4*pow(sine(x/3),3)

def countdown_up(n):
    """Starts at n and simultaneously prints out the countdown from n to 0
    and the countup from n to 2*n, inclusive.

    >>> countdown_up(0)
    0

    >>> countdown_up(5)
    5
    4
    6
    3
    7
    2
    8
    1
    9
    0
    10
    """
    def count(i):
        if i == 0:
            print(n)
        elif i > n:
            return
        else:
            print(n-i)
            print(n+i)
        count(i+1)
    count(0)

def mario_number(level):
    """Return the number of ways that Mario can perform a sequence of steps
    or jumps to reach the end of the level without ever landing in a Piranha
    plant. Assume that every level begins and ends with a space.

    >>> mario_number(' P P ')   # jump, jump
    1
    >>> mario_number(' P P  ')   # jump, jump, step
    1
    >>> mario_number('  P P ')  # step, jump, jump
    1
    >>> mario_number('   P P ') # step, step, jump, jump or jump, jump, jump
    2
    >>> mario_number(' P PP ')  # Mario cannot jump two plants
    0
    >>> mario_number('    ')    # step, jump ; jump, step ; step, step, step
    3
    >>> mario_number('    P    ')
    9
    >>> mario_number('   P    P P   P  P P    P     P ')
    180
    """
    def ways(n):
        if n == len(level)-1:
            return 1
        if n >= len(level) or level[n] == 'P':
            return 0
        return ways(n+1) + ways(n+2)

    return ways(0)

def knapsack(weights, values, c):
    """
    >>> w = [2, 6, 3, 3]
    >>> v = [1, 5, 3, 3]
    >>> knapsack(w, v, 6)
    6
    """
    if weights == []:
        return 0
    else:
        first_weight, rest_weights = weights[0], weights[1:]
        first_value, rest_values = values[0], values[1:]
        with_first = first_value + knapsack(rest_weights, rest_values, c-first_weight)
        without_first = knapsack(rest_weights, rest_values, c)
        if first_weight <= c:
            return max(with_first, without_first)
        return without_first

from operator import sub, mul

def Y(f):
    """The Y ("paradoxical") combinator."""
    return f(lambda: Y(f))

def Y_tester():
    """
    >>> tmp = Y_tester()
    >>> tmp(1)
    1
    >>> tmp(5)
    120
    >>> tmp(2)
    2
    """
    return Y(lambda f: lambda n: 1 if n==0 else mul(n, f()(sub(n, 1))))

if __name__ == "__main__":
    import doctest
    doctest.testmod()