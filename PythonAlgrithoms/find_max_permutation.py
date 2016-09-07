from collections import Counter
from collections import defaultdict


def naive_max_perm(M, A=None):
    # recursive version O(n2)
    if A is None:
        A = set(range(len(M)))
    if len(A) == 1:
        return A
    B = set(M[i] for i in A)
    C = A - B
    if C:
        A.remove(C.pop())
        return naive_max_perm(M, A)
    return A


def max_perm_itor(M, A=None):
    # iterator version transformed directly from recursive version O(n2)
    if A is None:
        A = set(range(len(M)))
    C = A - set(M[i] for i in A)
    while C:
        A.remove(C.pop())
        C = A - set(M[i] for i in A)
    return A


def max_perm(M):
    # like pointers counting O(n)
    n = len(M)
    A = set(range(n))
    count = [0] * n
    for i in M:
        count[i] += 1
    Q = [i for i in A if count[i] == 0]
    while Q:
        i = Q.pop()
        A.remove(i)
        j = M[i]
        count[j] -= 1
        if count[j] == 0:
            Q.append(j)
    return A


def max_perm_readable(M):
    A = set(range(len(M)))
    count = defaultdict(int)
    for k, v in Counter(M).items():
        count[k] = v
    Q = filter(lambda i: count[i] == 0, A)
    while Q:
        useless_elt = Q.pop()
        A.remove(useless_elt)
        elt_pointed_by_useless_elt = M[useless_elt]
        count[elt_pointed_by_useless_elt] -= 1
        if count[elt_pointed_by_useless_elt] == 0:
            Q.append(elt_pointed_by_useless_elt)
    return A


def main():
    M = [2, 2, 0, 5, 3, 5, 7, 4]
    print naive_max_perm(M)
    # >> set([0, 2, 5])
    print max_perm_itor(M)
    print max_perm(M)
    print max_perm_readable(M)

if __name__ == '__main__':
    main()
