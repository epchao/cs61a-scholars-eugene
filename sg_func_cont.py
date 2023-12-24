# Q14: Same hailstone

def same_hailstone(a, b):
    """Return whether a and b are both members of the same hailstone
    sequence.

    >>> same_hailstone(10, 16) # 10, 5, 16, 8, 4, 2, 1
    True
    >>> same_hailstone(16, 10) # order doesn't matter
    True
    >>> result = same_hailstone(3, 19) # return, don't print
    >>> result
    False


    Extra tests:

    >>> same_hailstone(19, 3)
    False
    >>> same_hailstone(4858, 61)
    True
    >>> same_hailstone(7, 6)
    False
    """
    return in_hailstone(a, b) or in_hailstone(b, a)

def in_hailstone(a, b):
    while a > 1:
        if a == b:
            return True
        elif a % 2 == 0:
            a //= 2
        else:
            a = a * 3 + 1
    
    return False

# Q15: Nearest Power of Two
def nearest_two(x):
    """Return the power of two that is nearest to x.

    >>> nearest_two(8)    # 2 * 2 * 2 is 8
    8.0
    >>> nearest_two(11.5) # 11.5 is closer to 8 than 16
    8.0
    >>> nearest_two(14)   # 14 is closer to 16 than 8
    16.0
    >>> nearest_two(2015)
    2048.0
    >>> nearest_two(.1)
    0.125
    >>> nearest_two(0.75) # Tie between 1/2 and 1
    1.0
    >>> nearest_two(1.5)  # Tie between 1 and 2
    2.0

    """
    power_of_two = 1.0

    if x < 1:
        factor = 0.5
    else:
        factor = 2
    while abs(power_of_two * factor - x) < abs(power_of_two - x):
        power_of_two *= factor
    if abs(power_of_two * 2 - x) == abs(power_of_two - x):
        power_of_two *= 2
    return power_of_two

from math import pi

def pi_fraction(gap):
    """Print the fraction within gap of pi that has the smallest denominator.

    >>> pi_fraction(0.01)
    22 / 7 = 3.142857142857143
    >>> pi_fraction(1)
    3 / 1 = 3.0
    >>> pi_fraction(1/8)
    13 / 4 = 3.25
    >>> pi_fraction(1e-6)
    355 / 113 = 3.1415929203539825

    """
    numerator, denominator = 3, 1
    while abs(numerator/denominator-pi) > gap:
        denominator += 1
        numerator = round(pi * denominator)

    print(numerator, '/', denominator, '=', numerator/denominator)

def count_one(n):
    """Counts the number of 1s in the digits of n

    >>> count_one(7007)
    0
    >>> count_one(123)
    1
    >>> count_one(161)
    2
    >>> count_one(1)
    1
    """
    count = 0

    while n:
        if n % 10 == 1:
            count += 1
        n //= 10

    return count

def total_ones(n):
    """Returns number of 1s in the digits of all numbers from 1 to
    n.

    >>> total_ones(10) # 1, 10 -> two 1s
    2
    >>> total_ones(15) # 1, 10, 11, 12, 13, 14, 15 -> eight 1s
    8
    >>> total_ones(21)
    13
    """
    count, total = 1, 0

    while count <= n:
        total += count_one(count)

        count += 1
    
    return total

def mul_by_num(num):
    """
    Returns a function that takes one argument and returns num
    times that argument.
    >>> x = mul_by_num(5)
    >>> y = mul_by_num(2)
    >>> x(3)
    15
    >>> y(-4)
    -8
    """
    return lambda x: num * x

if __name__ == "__main__":
    import doctest
    doctest.testmod()