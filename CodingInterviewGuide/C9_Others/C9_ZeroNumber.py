def zero_number(n):
    if n < 0:
        return 0
    res = 0
    while n:
        res += n / 5
        n /= 5
    return res


# how many zeros 10! contains
print zero_number(10)
