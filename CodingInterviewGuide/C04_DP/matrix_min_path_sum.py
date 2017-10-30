m = [
    [1, 3, 5, 9],
    [8, 1, 3, 4],
    [5, 0, 6, 1],
    [8, 8, 4, 0],
]

assert len(m) > 1
len_row = len(m)
len_column = len(m[0])

dp = [[0] * len_column for _ in range(len_row)]

for i in range(0, len_row):
    for j in range(0, len_column):
        if i == 0:
            dp[i][j] = dp[i][j - 1] + m[i][j] if j > 0 else m[i][j]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + m[i][j] if j > 0 else dp[i - 1][j] + m[i][j]

print(dp[-1][-1])

for i in range(0, len_row):
    for j in range(0, len_column):
        if i == 0:
            if j == 0:
                already = 0
            else:
                already = dp[i][j - 1]
        else:
            if j == 0:
                already = dp[i - 1][j]
            else:
                already = min(dp[i - 1][j], dp[i][j - 1])
        dp[i][j] = already + m[i][j]

print(dp[-1][-1])
