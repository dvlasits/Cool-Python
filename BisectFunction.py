# Lets say we want to binary search over a func
from bisect import bisect_left


class Test:

    def func(self, x):
        return x > 10

    def __getitem__(self, item):
        return self.func(item)


x = Test()

print(bisect_left(x, True, 0, 1000))
