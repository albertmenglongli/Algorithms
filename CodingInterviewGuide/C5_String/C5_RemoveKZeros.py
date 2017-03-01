def remove_k_zeros(s, k):
    eles = list(s)
    cnt = 0
    start = -1
    for idx, c in enumerate(eles):
        if c == '0':
            cnt += 1
        else:
            if cnt == k and idx - 1 >= 0 and eles[idx - 1] == '0':
                for i in range(start + 1, start + k + 1):
                    eles[i] = 'N/A'
            start = idx
            cnt = 0
    if cnt == k:
        for i in range(start + 1, start + k + 1):
            eles[i] = 'N/A'
    return ''.join((e for e in eles if e != 'N/A'))


assert remove_k_zeros('000A00B000', 3) == 'A00B'
assert remove_k_zeros('000A00B000', 2) == '000AB000'
