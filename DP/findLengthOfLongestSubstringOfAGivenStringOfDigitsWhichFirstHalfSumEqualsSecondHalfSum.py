class Solution(object):
    def find_max_length(self, s):
        n = len(s)
        my_sum = [[0] * n for _ in range(n)]
        max_len = 0
        for i in range(0, n):
            my_sum[i][i] = ord(s[i]) - ord('0')
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                first_half_sum = my_sum[i][i + length // 2 - 1]
                second_half_sum = my_sum[i + length // 2][i + length - 1]
                my_sum[i][i + length - 1] = first_half_sum + second_half_sum
                if length % 2 == 0 and first_half_sum == second_half_sum and length > max_len:
                    max_len = length
        return max_len

    def find_max_length2(self, s):
        n = len(s)
        my_sum = [[0] * n for _ in range(n)]
        max_len = 0
        for i in range(0, n):
            my_sum[i][i] = ord(s[i]) - ord('0')
        for i in range(n - 1, -1, -1):
            for m in range(i + 1, n):
                my_sum[i][m] = my_sum[i + 1][m] + my_sum[i][i]
            for j in range(i + 1, n):
                length = j - i + 1
                first_half_sum = my_sum[i][i + length // 2 - 1]
                second_half_sum = my_sum[i + length // 2][j]
                if length % 2 == 0 and first_half_sum == second_half_sum and length > max_len:
                    max_len = length
        return max_len

    def find_max_length3(self, s):
        n = len(s)
        my_sum = [[0] * n for _ in range(n)]
        max_len = 0
        for i in range(0, n):
            my_sum[i][i] = ord(s[i]) - ord('0')
        for i in range(n - 1, -1, -1):  # i: the start idx of the sub string
            for j in range(i + 1, n):  # j: the end idx of the sub string
                # update my_sum[i][j] due to s[i] prepended to the heading of the substring (idx from i+1 to j)
                # which has already been calculated last i-loop
                my_sum[i][j] = my_sum[i + 1][j] + my_sum[i][i]
                length = j - i + 1
                if length % 2 == 0:
                    first_half_sum = my_sum[i][i + length // 2 - 1]
                    second_half_sum = my_sum[i + length // 2][j]
                    if first_half_sum == second_half_sum and length > max_len:
                        max_len = length
        return max_len


# 三种方式本质一样, 还是觉得第一种更好理解
assert Solution().find_max_length('142124') == 6
assert Solution().find_max_length('9430723') == 4
assert Solution().find_max_length2('142124') == 6
assert Solution().find_max_length2('9430723') == 4
assert Solution().find_max_length3('9430723') == 4
assert Solution().find_max_length3('142124') == 6
