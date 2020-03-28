def edit_distance(str1, str2):
    if str1 and str2:
        if str1[0] == str2[0]:
            return edit_distance(str1[1:], str2[1:])
        else:
            # by inserting
            tmp1 = 1 + edit_distance(str1, str2[1:])
            # by deleting
            tmp2 = 1 + edit_distance(str1[1:], str2)
            # by replacing
            tmp3 = 1 + edit_distance(str1[1:], str2[1:])
            return min(tmp1, tmp2, tmp3)
    else:
        return len(str1) or len(str2)


def edit_distance_dp(str1, str2):
    l1 = len(str1)
    l2 = len(str2)

    EditD = [[0] * (l1 + 1) for _ in range(l2 + 1)]

    for i in range(l1 + 1):
        EditD[0][i] = i
    for i in range(l2 + 1):
        EditD[i][0] = i

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if str1[i - 1] == str2[j - 1]:
                EditD[j][i] = EditD[j - 1][i - 1]
            else:
                EditD[j][i] = min(EditD[j - 1][i - 1], EditD[j][i - 1], EditD[j - 1][i]) + 1

    return EditD[l2][l1]


if __name__ == '__main__':
    assert edit_distance('SUNDAY', 'SATURDAY') == 3
    assert edit_distance('CAT', 'CAR') == 1

    assert edit_distance_dp('SUNDAY', 'SATURDAY') == 3
    assert edit_distance_dp('CAT', 'CAR') == 1
