def counting_sort(A, key=lambda x: x):
    from collections import defaultdict
    B, C = [], defaultdict(list)
    for x in A:
        C[key(x)].append(x)
    for k in range(min(C), max(C) + 1):
        B.extend(C[k])
    return B


def counting_sort_int(A):
    from collections import defaultdict, Counter
    B, C = [], defaultdict(int, Counter(A))
    [B.extend([k] * C[k]) for k in range(min(C), max(C) + 1)]
    return B


class Obj(object):

    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return True if other and isinstance(other, Obj) and self.val == other.val else False

    def __hash__(self):
        return self.val


def main():
    import random
    lst = list(range(0, 100)) + list(range(0, 100))
    random.shuffle(lst)
    print(counting_sort(lst))
    print(counting_sort_int(lst))
    lst = [Obj(3), Obj(4), Obj(3)]
    sorted_objs = counting_sort(lst, key=lambda x: x.val)
    for obj in sorted_objs:
        print(obj.val)
    # >> 3 3 4


if __name__ == '__main__':
    main()
