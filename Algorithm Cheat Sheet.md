# Algorithm Cheat Sheet

## 2D-array

```
# table of n x m 
table = [[0] * m for _ in range(n)]
```

```
# table with row idx: 0 ... n, and column idx: 0 ... m
table = [[0] * (m + 1) for _ in range(n + 1)]
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

```
def memo(func):
    cache = {}
    
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap
```


## defaultdict
```
from collections import defaultdict
tree = lambda: defaultdict(tree)
root = tree()
root['a']['b'] = 'xx'
```

## dict

```
dict.fromkeys(['a','b','c'], -1)
# {'a': -1, 'b': -1, 'c': -1}
```

```
dict(zip(keys, values))
```

## division

```
-3 / -4 = -1 # -> float('-inf')
```

## math

```
import math
math.pow(2, 3) # 8
math.sqrt(4) # 2
math.ceil(1.3) # 2
math.floor(1.3) #1
```

## random

```
import random
random.random() # [0.0, 1.0)
random.randint(0, 5) # 0, 1, 2, 3, 4
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
