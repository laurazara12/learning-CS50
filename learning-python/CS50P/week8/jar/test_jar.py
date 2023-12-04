from jar import Jar
import pytest

def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()

def test_init():
    jar = Jar(5)
    assert jar.jar_capacity == 5

def test_str():
    jar = Jar(5)
    jar.deposit(3)
    jar.withdraw(1)
    assert str(jar) == "🍪🍪"

def test_withdraw():
    jar = Jar(5)
    jar.withdraw(0)
    assert jar.number_cookies == 0

def test_deposit():
    jar = Jar(5)
    jar.deposit(2)
    assert jar.number_cookies == 2

if __name__ == "__main__":
    main()