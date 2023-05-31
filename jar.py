#A program that simulates a cookie jar, which has both a capacity and amount of cookies. It can depict the number of cookies in the jar at any given time using emojis.

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if n > self._capacity:
            raise ValueError("Too many cookies!")
        if self._size + n > self._capacity:
            raise ValueError("Too many cookies!")
        self._size += n

    def withdraw(self, n):
        if self._size < n:
            raise ValueError("Not enough cookies :(")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size