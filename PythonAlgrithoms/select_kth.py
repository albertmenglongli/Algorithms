lst = [0, 1, 2, 3, 4, 5, 6, 7]


def partition(seq):
    pi = seq[0]
    seq = seq[1:]
    lo = [e for e in seq if e <= pi]
    hi = [e for e in seq if e > pi]
    return lo, pi, hi


def select(seq, k):
    lo, pi, hi = partition(seq)
    m = len(lo)
    if m == k:
        return pi
    elif m < k:
        return select(hi, k - m - 1)
    else:
        return select(lo, k)


if __name__ == '__main__':
    seq = lst
    k = 4
    res = select(seq, k)
    print(res)
