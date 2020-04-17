def memo(func):
    cache = {}

    def inner(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return inner


@memo
def recurse(times, score):
    if times <= 0 or score < 0:
        return 0

    if times == 1:
        return 1

    res = 0
    for i in range(0, 11):
        if score - i <= (times - 1) * 10:
            res += recurse(times - 1, score - i)
    return res


if __name__ == '__main__':
    # print(recurse(10, 80))
    # print(recurse(2, 18))
    # print(recurse(2, 20))
    # print(recurse(1, 0))
    print(recurse(2, 11))
