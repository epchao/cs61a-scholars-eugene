def typewriter(word):
    """A function that keeps track of a word as it's being typed."
    >>> t = typewriter("he")
    he
    >>> t = t("llo")
    hello
    >>> t = t(" w")
    hello w
    >>> t = t("orld!")
    hello world!
    """
    def typing(next_str):
        new_word = word + next_str
        return typewriter(new_word)
    print(word)
    return typing

def protected_secret(password, secret, num_attempts):
    """
    Returns a function which takes in a password and prints the SECRET if the password entered matches
    the PASSWORD given to protected_secret. Otherwise it prints "INCORRECT PASSWORD". After NUM_ATTEMPTS
    incorrect passwords are entered, the secret is locked and the function should print "SECRET LOCKED".

    >>> my_secret = protected_secret("correcthorsebatterystaple", "I love UCB", 2)
    >>> my_secret = my_secret("hax0r_1") # 2 attempts left
    INCORRECT PASSWORD
    >>> my_secret = my_secret("correcthorsebatterystaple")
    I love UCB
    >>> my_secret = my_secret("hax0r_2") # 1 attempt left
    INCORRECT PASSWORD
    >>> my_secret = my_secret("hax0r_3") # No attempts left
    SECRET LOCKED
    >>> my_secret = my_secret("correcthorsebatterystaple")
    SECRET LOCKED
    """
    def get_secret(password_attempt):
        if num_attempts <= 0:
            print("SECRET LOCKED")
            return protected_secret(password, secret, num_attempts - 1)
        elif password_attempt == password:
            print(secret)
            return protected_secret(password, secret, num_attempts)
        else:
            print("INCORRECT PASSWORD")
            return protected_secret(password, secret, num_attempts - 1)
    return get_secret

def composer(func=lambda x: x):
    """
    Returns two functions -
    one holding the composed function so far, and another
    that can create further composed problems.
    >>> add_one = lambda x: x + 1
    >>> mul_two = lambda x: x * 2
    >>> f, func_adder = composer()
    >>> f1, func_adder = func_adder(add_one)
    >>> f1(3)
    4
    >>> f2, func_adder = func_adder(mul_two)
    >>> f2(3) # should be 1 + (2*3) = 7
    7
    >>> f3, func_adder = func_adder(add_one)
    >>> f3(3) # should be 1 + (2 * (3 + 1)) = 9
    9
    """
    def func_adder(g):
        return composer(lambda x: func(g(x)))
        
    return func, func_adder

def both_paths(sofar="S"):
    """
    >>> up, down = both_paths()
    S
    >>> upup, updown = up()
    SU
    >>> downup, downdown = down()
    SD
    >>> _ = upup()
    SUU
    """
    print(sofar)
    def up():
        return both_paths(sofar + "U")

    def down():
        return both_paths(sofar + "D")

    return up, down   

if __name__ == "__main__":
    import doctest
    doctest.testmod()