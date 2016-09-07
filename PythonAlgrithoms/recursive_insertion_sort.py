# recursive version
def ins_sort_rec(seq, i):
    if i == 0:
        return
    ins_sort_rec(seq, i - 1)
    j = i
    while j > 0 and seq[j - 1] > seq[j]:
        seq[j - 1], seq[j] = seq[j], seq[j - 1]
        j -= 1

# non-recursive version
def ins_sort(seq):
    for i in range(0, len(seq)):
        j = i
        while j > 0 and seq[j - 1] > seq[j]:
            seq[j - 1], seq[j] = seq[j], seq[j - 1]
            j -= 1


def main():
    import random
    lst = range(0, 100)

    random.shuffle(lst)
    ins_sort_rec(lst, 99)
    print lst

    random.shuffle(lst)
    ins_sort(lst)
    print lst


if __name__ == '__main__':
    main()
