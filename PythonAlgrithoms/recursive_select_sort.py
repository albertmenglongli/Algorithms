# the recursive version for selection sort
def sel_sort_rec(seq, i):
    if i == 0:
        return
    j_max = i
    for j in range(i):
        if seq[j] > seq[j_max]:
            j_max = j
    seq[i], seq[j_max] = seq[j_max], seq[i]
    sel_sort_rec(seq, i - 1)


# inter-version
def sel_sort(seq):
    for i in range(len(seq) - 1, 0, -1):
        j_max = i
        for j in range(i):
            if seq[j] > seq[j_max]:
                j_max = j
        seq[i], seq[j_max] = seq[j_max], seq[i]


def main():
    import random
    lst = range(0, 100)

    random.shuffle(lst)
    sel_sort_rec(lst, 99)
    print lst

    random.shuffle(lst)
    sel_sort(lst)
    print lst

if __name__ == '__main__':
    main()
