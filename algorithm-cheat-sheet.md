# Algorithm Cheat Sheet

## 2D-array

```
# table of n x m 
table = [[0] * m for _ in range(n)]
```

```
# table with row idx: 0 ... n, and column idx: 0 ... m
# table of (n + 1) * (m + 1)
table = [[0] * (m + 1) for _ in range(n + 1)]
```

```
# table of n x m
import numpy as np
table = np.zeros((n, m), int)
```

## bisect/ bisearch

```
import bisect
bisect.bisect_left(arr, x, lo=0, hi=len(arr))

bisect.bisect(arr, x, lo=0, hi=len(arr))
bisect.bisect_right(arr, x, lo=0, hi=len(arr))
```

```
def bisect_left(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

```
def bisect_right(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]: 
            hi = mid
        else: 
            lo = mid+1
    return lo
```


```
def bisearch(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = start + (end - start) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1
```

## cache

support only args parameters

```
def memo(func):
    cache = {}
    
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap
```

support both args and kwargs parameters

```
def memo(func):
    import json
    import hashlib
    try:
        from inspect import signature
    except ImportError:
        from funcsigs import signature

    cache = {}

    def wrap(*args, **kwargs):
        sig = signature(func)
        params_ordered_dict = sig.bind(*args, **kwargs).arguments
        json_str = json.dumps(dict(params_ordered_dict), sort_keys=True)
        cache_key = hashlib.sha256(json_str.encode('utf-8')).hexdigest()
        if cache_key not in cache:
            cache[cache_key] = func(*args, **kwargs)
        return cache[cache_key]

    return wrap
```

## defaultdict
```
from collections import defaultdict
tree = lambda: defaultdict(tree)
root = tree()
root['a']['b'] = 'xx'
```

defaultdict with customised value(not the default one from type)

```
from collections import defaultdict
d = defaultdict(lambda: -1, {})
```

## dict

```
dict.fromkeys(['a','b','c'], -1)
# {'a': -1, 'b': -1, 'c': -1}
```

```
dict(zip(keys, values))
```

```
class Bunch(dict):
    def __init__(self, *args, **kwargs):
        super(Bunch, self).__init__(*args, **kwargs)
        self.__dict__ = self

Node = Bunch
n = Node(value=1, left=Node(value=2, left=None, right=None), right=Node(value=3, left=None, right=None))

# {
#     "right": {
#         "right": None,
#         "value": 3,
#         "left": None
#     },
#     "value": 1,
#     "left": {
#         "right": None,
#         "value": 2,
#         "left": None
#     }
# }
```

## deque
```
from collections import deque
q = deque()
q.append(1)
q.appendleft(-1)
q.pop()
q.popleft()
q.extend([4, 5, 6])
q.extendleft([3, 2, 1])
```

## division

```
-3 / -4 = -1 # -> float('-inf')
```

## Graph General Traverse

```
def traverse_generator(G, s, qtype=set):
    Seen, Q = set(), qtype()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in Seen:
            continue
        Seen.add(u)
        for v in G[u]:
            Q.add(v)
        yield u


def traverse(G, s, qtype=set):
    Seen, Q = set(), qtype()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in Seen:
            continue
        Seen.add(u)
        for v in G[u]:
            Q.add(v)
    return Seen

G = {
    'a': ['b', 'c', 'd'],
    'b': ['a', 'd'],
    ...
    ...
}


print list(traverse_generator(G, 'a'))
print traverse(G, 'a')

class stack(list):
    add = list.append

print list(traverse_generator(G, 'a', stack))
```


## Graph Commponents
```
def components(G):
    def walk(s, F=set()):
        P, Q = dict(), set()
        P[s] = None
        Q.add(s)
        while Q:
            u = Q.pop()
            for v in G[u].difference(P, F):
                Q.add(v)
                P[v] = u
        return P

    comp = []
    seen = set()
    for u in G:
        if u in seen:
            continue
        C = walk(u)
        seen.update(C)
        comp.append(C)
    return comp


G = {
    'a': {'b', 'c', 'd'},
    'b': {'a', 'd'},
    'c': {'a', 'd'},
    'd': {'a', 'b', 'c'},
    'e': {'f', 'g'},
    'f': {'e', 'g'},
    'g': {'f', 'e'},
    'h': {'i'},
    'i': {'h'}
}

print components(G)
```

## heapq

```
import heapq
# heap is a list
heapq.heapify(heap)
heappush(heap, item)
heapq.heappush(heap, (weight, obj))
heap[0] # peek: the element at idx 0 is always the smallest
heapq.heappop()
heapq.nlargest(n, iterable[, key])
heapq.nsmallest(n, iterable[, key])
heapq.heappushpop(h, item) # push, then pop
heapq.heapreplace(h, item) # pop, then push
```

## math

```
import math
math.pow(2, 3) # 8
math.sqrt(4) # 2
math.ceil(1.3) # 2
math.floor(1.3) #1
```

## OrderedDict

```
from collections import OrderedDict
d = OrderedDict()
d.popitem(last=True)
```

## random

```
import random
random.random() # [0.0, 1.0)
random.randint(0, 5) # 0, 1, 2, 3, 4
```

## set

```
s.update(iterable)
s.add(item)
s.remove(item)
s.discard(item) # remove if exist else do nothing
s.difference(*iterables) # -
s.difference_update(*iterables)
s.intersection(*iterables) # +
```

## sort

```
a = range(5, -1, -1)
a.sort()  # sort in-place
b = sorted(a)  # return a new sorted list
```

## while-loop

```
// in Java/C++
do{
...
...
} while (expression)
```
in Python:
```
while True:
    ...
    ...
    if not expression:
        break
```

## tail-call-optimized

```
import sys
from functools import wraps


class TailRecurseException(Exception):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(func):

    @wraps(func)
    def inner_wrapper(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            while 1:
                try:
                    return func(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs

    return inner_wrapper


@tail_call_optimized
def factorial(n, acc=1):
    if n == 0:
        return acc
    return factorial(n - 1, n * acc)


print(factorial(10001))

```