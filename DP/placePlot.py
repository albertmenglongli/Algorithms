def count_ways_2n_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return count_ways_2n_rec(n - 1) + count_ways_2n_rec(n - 2)


def count_ways_2n(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b = 1, 2
    c = None
    for i in range(n - 2):
        c = a + b
        a, b = b, c
    return c


def count_ways_3n_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 3
    if n == 3:
        return 2

    # return count_ways_3n_rec(2) * count_ways_3n_rec(n - 2) + count_ways_3n_rec(3) * count_ways_3n_rec(n - 3)
    # 当n为4的时候，不能按1+3来拆分，此时公式后半部分为0，仍满足条件，相当于
    # if n == 4: return count_ways_3n_rec(2) * count_ways_3n_rec(2)
    return 3 * count_ways_3n_rec(n - 2) + 2 * count_ways_3n_rec(n - 3)


def count_ways_3n(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 3
    if n == 3:
        return 2
    if n == 4:
        return 9

    a, b, c = 3, 2, 9
    d = None
    for i in range(n - 4):
        d = 2 * a + 3 * b
        a, b, c = b, c, d
    return d


if __name__ == '__main__':
    # Example 8.2
    print(count_ways_2n_rec(1))
    print(count_ways_2n_rec(2))
    print(count_ways_2n_rec(3))
    print(count_ways_2n_rec(4))
    print(count_ways_2n_rec(5))
    print()

    print(count_ways_2n(1))
    print(count_ways_2n(2))
    print(count_ways_2n(3))
    print(count_ways_2n(4))
    print(count_ways_2n(5))
    print()

    # Question 8.2
    print(count_ways_3n_rec(4))
    print(count_ways_3n_rec(5))
    print(count_ways_3n_rec(6))
    print(count_ways_3n_rec(7))
    print()

    print(count_ways_3n(4))
    print(count_ways_3n(5))
    print(count_ways_3n(6))
    print(count_ways_3n(7))
