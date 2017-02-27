# judge if s is None or empty
# judge if s represent all digits and not start with 0
# judge if s contains - at first, and the following is not 0
# judge if s is too large, beyond 32 bit, how big is big
# valid range is -(2**31) -> 2**31 - 1


def is_valid(s):
    MAX = 2 ** 31 - 1
    MIN = - 2 ** 31
    if not s or s.startswith('0') or (s.startswith('-') and len(s) == 1) or (s.startswith('-') and s[1] == '0'):
        return 0
    negative = True if s.startswith('-') else False
    s = s if not negative else ''.join(s[1:])
    if not s.isdigit():
        return 0
    number = 0
    for idx, c in enumerate(s):
        number *= 10
        if negative:
            number -= int(c)
        else:
            number += int(c)
        if number > MAX or number < MIN:
            return 0

    return number


assert is_valid('') == 0
assert is_valid('A') == 0
assert is_valid('0') == 0
assert is_valid('-0') == 0
assert is_valid('-123') == -123
assert is_valid('435523') == 435523
assert is_valid(str(2 ** 32)) == 0
