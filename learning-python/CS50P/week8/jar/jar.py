class Jar:
    """
    __init__ should initialize a cookie jar with the given capacity,
    which represents the maximum number of cookies that can fit in the cookie jar.
    If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
    """
    def __init__(self, capacity=12):
        self.number_cookies = 0
        if capacity >=0:
            self.jar_capacity = capacity
        else:
            raise ValueError("Negative capacity")
    """
    __str__ should return a str with🍪, where
    is the number of cookies in the cookie jar. For instance,
    if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
    """
    def __str__(self):
        return "🍪" * self.number_cookies
    """
    deposit should add n cookies to the cookie jar.
    If adding that many would exceed the cookie jar’s
    capacity, though, deposit should instead raise a ValueError.
    """
    def deposit(self, n):
        if self.number_cookies + n <= self.jar_capacity:
            self.number_cookies += n
        else:
            raise ValueError("Max. capacity excceded")
    """
    withdraw should remove n cookies from the cookie jar.
    Nom nom nom. If there aren’t that many cookies in the cookie jar,
    though, withdraw should instead raise a ValueError.
    """
    def withdraw(self, n):
        if self.number_cookies >= n:
            self.number_cookies -= n
        else:
            raise ValueError("Min. capacity excceded")
    """
    capacity should return the cookie jar’s capacity.
    """
    @property
    def capacity(self):
        return self.jar_capacity
    """
    size should return the number of cookies actually
    in the cookie jar, initially 0.
    """
    @property
    def size(self):
        return self.number_cookies

def main():
    jar = Jar(5)
    jar.deposit(3)
    jar.withdraw(1)
    print(jar)

if __name__ == "__main__":
    main()