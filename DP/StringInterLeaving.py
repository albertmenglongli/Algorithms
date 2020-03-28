def is_inter_leaving(str1, str2, str3) -> bool:
    if len(str3) != len(str1) + len(str2):
        return False

    if not str1:
        return str2 == str3

    if not str2:
        return str1 == str3

    if str1[0] == str2[0] == str3[0]:
        return is_inter_leaving(str1[1:], str2, str3[1:]) or is_inter_leaving(str1, str2[1:], str3[1:])

    elif str3[0] == str1[0]:
        return is_inter_leaving(str1[1:], str2, str3[1:])

    elif str3[0] == str2[0]:
        return is_inter_leaving(str1, str2[1:], str3[1:])
    else:
        # str3[0] != str1[0] and str3[0] != str2[0]
        return False


def is_inter_leaving_dp(str1, str2, str3) -> bool:
    if len(str3) != len(str1) + len(str2):
        return False

    Mat = [[False] * (len(str1) + 1) for __ in range(len(str2) + 1)]
    Mat[0][0] = True

    for i in range(1, len(str1) + 1):
        if str1[i - 1] != str3[i - 1]:
            Mat[0][i] = False
        else:
            Mat[0][i] = Mat[0][i - 1]

    for i in range(1, len(str2) + 1):
        if str2[i - 1] != str3[i - 1]:
            Mat[i][0] = False
        else:
            Mat[i][0] = Mat[i - 1][0]

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str1[j - 1] == str2[i - 1] == str3[i + j - 1]:
                Mat[i][j] = Mat[i - 1][j] or Mat[i][j - 1]
            elif str3[i + j - 1] == str1[j - 1]:
                Mat[i][j] = Mat[i][j - 1]
            elif str3[i + j - 1] == str2[i - 1]:
                Mat[i][j] = Mat[i - 1][j]
    return Mat[len(str2)][len(str1)]


if __name__ == '__main__':
    A = 'xyz'
    B = 'abcd'
    C = 'xabyczd'
    assert is_inter_leaving(A, B, C)

    A = 'xyz'
    B = 'abcd'
    C = 'xabyczd'
    assert is_inter_leaving_dp(A, B, C)

    A = 'bbca'
    B = 'bcc'
    C = 'bbcbcac'
    assert is_inter_leaving_dp(A, B, C)
