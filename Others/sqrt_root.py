def sqrt_root(num):
    if num == 0 or num == 1:
        return 1
    low = 0.0
    high = float(num) if num > 1 else 1
    x = 0.0

    while low <= high:
        x = (low + high) / 2
        if x * x > num:
            high = x - 0.0001
        elif x * x < num:
            low = x + 0.0001
        else:
            break

    return round(x, 3)


print(sqrt_root(2))
print(sqrt_root(0.5))
print(sqrt_root(0.00000001))
import math

print(math.sqrt(2))
print(math.sqrt(0.5))
print(math.sqrt(0.00000001))
