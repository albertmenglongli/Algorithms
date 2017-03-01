class Solution(object):

    def cut_rod(self, values, n):
        max_arr = [0] * (n + 1)
        for i in range(1, n + 1):
            for idx, value in enumerate(values):
                length = idx + 1
                if length <= i:
                    max_arr[i] = max(max_arr[i], max_arr[i - length] + value)
        print max_arr
        return max(max_arr)


values = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8

print Solution().cut_rod(values, n)
