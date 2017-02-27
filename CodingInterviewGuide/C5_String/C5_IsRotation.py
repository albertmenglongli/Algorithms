def is_rotation(s1, s2):
    if not s1 or not s2:
        return False
    if len(s1) != len(s2):
        return False
    return s1 in s2 + s2


assert is_rotation('abcd', 'cdab')
assert not is_rotation('abcd', 'abdd')
assert not is_rotation(None, '')
