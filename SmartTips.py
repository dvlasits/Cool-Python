x = "Testing This Th List"
print(x.find("Th", 1, 5))  # Can give index for start and end
# Returns index of first occurence

dic = {}

for key, value in dic.items():
    pass

import heapq

myHeap = [5, 1]
heapq.heapify(myHeap)
heapq.heappush(myHeap, 5)
print(heapq.heappop(myHeap))

import bisect

print(
    bisect.bisect_left([1, 4, 8, 10], 5))  # Gives position value should be inserted and before any values that match it

from collections import defaultdict, Counter, deque

a = defaultdict(set)
b = Counter([1, 1, 1, 2, 2, 2, 6])
print(b)

c = deque()
c.append(5)
c.appendleft(10)
c.extend(range(1, 10))
c.extendleft(range(1, 10))
c.pop(), c.popleft()
print(c)

# Using min and max as argmax and argmin
# min will get leftmost occurence and max will get rightmost

valmin, argmin = min((x, i) for i, x in enumerate(range(10)))
# Do max of the negative values if you want the rightmost one

from functools import lru_cache


@lru_cache(maxsize=None)
def test():
    pass


# Can do binary search of a continuous function too!!!!!!
def continous_binary_search(f, lo, hi, gap=1e-4):
    while hi - lo > gap:
        mid = (lo + hi) / 2.0
        if f(mid):
            hi = mid
        else:
            lo = mid
    return lo

#CAN DO this if don't know the range with monotonic function just keep doubling until bigger

