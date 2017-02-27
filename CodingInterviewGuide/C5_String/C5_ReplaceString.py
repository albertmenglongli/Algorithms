def replace(s, _from, _to):
    if not s or not _from or not _to:
        return s
    match_idx = 0
    eles = list(s)
    for idx, c in enumerate(eles):
        if match_idx < len(_from) - 1 and c == _from[match_idx]:
            match_idx += 1
        elif match_idx == len(_from) - 1:
            for i in range(idx - match_idx, idx + 1):
                eles[i] = ''
            match_idx = 0
        else:
            match_idx = 0

    from copy import deepcopy
    new_eles = deepcopy(eles)
    for idx, c in enumerate(eles):
        if c:
            continue
        else:
            if idx - 1 >= 0 and eles[idx - 1] == '':
                continue
            else:
                new_eles[idx] = _to
    return ''.join(new_eles)


assert replace('123abcabc', 'abc', 'X') == '123X'
assert replace('123ab', 'abc', 'X') == '123ab'
