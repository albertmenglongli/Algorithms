def random_to_5():
    import random
    return random.randint(0, 5) + 1


def random_to_7():
    r = 0
    while True:
        c1 = random_to_5()
        c2 = random_to_5()

        r = (c1 - 1) * 5 + c2 - 1
        if r <= 20:
            break

    return r % 7 + 1


def random_01_p():
    import random
    res = random.random()
    return 0 if res < 0.83 else 1


def random_01():
    res = 0
    while True:
        res = random_01_p()
        if res != random_01_p():
            break
    return res
