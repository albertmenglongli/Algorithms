def mergesort(seq):
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1: lft = mergesort(lft)
    if len(rgt) > 1: rgt = mergesort(rgt)
    result = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            result.append(lft.pop())
        else:
            result.append(rgt.pop())
    result.reverse()
    return (lft or rgt) + result


if __name__ == "__main__":
    seq = [5, 2, 8, 1]
    print(mergesort(seq))
